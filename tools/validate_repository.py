"""Check local documentation targets, manifests and obvious publication leaks."""
import json
from pathlib import Path
import re
import os
from html.parser import HTMLParser
import xml.etree.ElementTree as ET
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []
def local_link(file, target):
    if target.startswith(('https://', 'http://', '#', 'mailto:')):
        return
    path = (file.parent / unquote(target.split('#')[0].split('?')[0])).resolve()
    if not path.is_relative_to(ROOT) or not path.exists():
        errors.append(f'Lien local absent : {file.relative_to(ROOT)} -> {target}')

class LocalLinks(HTMLParser):
    def __init__(self, file):
        super().__init__()
        self.file = file
    def handle_starttag(self, tag, attrs):
        for key, target in attrs:
            if key in {'href', 'src'} and target:
                local_link(self.file, target)

files = []
for directory, dirs, names in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in {'.git', '__pycache__', 'node_modules', '.venv', 'private', 'raw'}]
    files.extend(Path(directory)/name for name in names)
for file in files:
    if file.suffix in {'.md', '.json', '.txt', '.yml', '.html', '.js', '.cjs', '.css', '.svg'} or file.name == 'LICENSE':
        text = file.read_text(encoding='utf-8')
        for pattern in (r'[A-Za-z]:[\\/]+Users[\\/]', r'gh[pousr]_[A-Za-z0-9]{25,}', r'github_pat_[A-Za-z0-9_]{30,}', r'-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----'):
            if re.search(pattern, text):
                errors.append(f'Information privée potentielle : {file.relative_to(ROOT)}')
        if file.suffix == '.md':
            for target in re.findall(r'\]\(([^)]+)\)', text):
                local_link(file, target)
        if file.suffix == '.html':
            LocalLinks(file).feed(text)
        if file.suffix == '.svg':
            try:
                ET.fromstring(text)
            except ET.ParseError as error:
                errors.append(f'SVG incorrect : {file.name}: {error}')

procedure = json.loads((ROOT/'ai/procedure.json').read_text(encoding='utf-8'))
states = procedure['states']
ids = {state['id'] for state in states}
if len(ids) != len(states) or procedure.get('automatic_actions') is not False or procedure.get('flash_authorized') is not False:
    errors.append('États du guide IA incohérents ou autorisation automatique présente')
for state in states:
    if state.get('next') is not None and state['next'] not in ids:
        errors.append(f'Transition inconnue : {state["id"]}')
    if not state.get('required_observation') or not state.get('next_action'):
        errors.append(f'Observation/action absente : {state["id"]}')
    if state.get('source_section'):
        local_link(ROOT/'AGENTS.md', state['source_section'])
for name in ['parcours','identifier','cles']:
    if not (ROOT/f'assets/{name}.png').is_file():
        errors.append(f'PNG du PDF absent : {name}')

for label, count in [('usb1',13), ('usb2',21), ('usb3',517), ('audio1046',1)]:
    manifest = json.loads((ROOT / f'data/{label}-files.json').read_text(encoding='utf-8'))
    files = manifest['files']
    if len(files) != count or len({x['path'] for x in files}) != count:
        errors.append(f'Nombre de fichiers incorrect : {label}')
    for record in files:
        if not re.fullmatch('[0-9a-f]{64}', record['sha256']) or record['bytes'] < 0:
            errors.append(f'Empreinte/taille incorrecte : {label}/{record["path"]}')
usb3 = json.loads((ROOT / 'data/usb3-files.json').read_text(encoding='utf-8'))['files']
mapping = {x['path']: (x['bytes'], x['sha256']) for x in usb3}
donor = 'VehicleParameter/DCU/86140-42581/'
target = 'VehicleParameter/DCU/86140-47490/'
for path, values in mapping.items():
    if path.startswith(donor) and mapping.get(target+path[len(donor):]) != values:
        errors.append(f'Profil donneur/copie différent : {path}')
if sum(x['bytes'] for x in usb3) != 23477795418:
    errors.append('Taille totale USB3 incohérente')
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print('Liens Markdown/HTML, SVG, états IA, inventaires, copie du profil et contrôle de publication : OK')
