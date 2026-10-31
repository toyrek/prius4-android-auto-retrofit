"""Check local documentation targets, manifests and obvious publication leaks."""
import json
from pathlib import Path
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []
for file in ROOT.rglob('*'):
    if not file.is_file() or any(p in {'.git', '__pycache__'} for p in file.relative_to(ROOT).parts):
        continue
    if file.suffix in {'.md', '.json', '.txt', '.yml'} or file.name == 'LICENSE':
        text = file.read_text(encoding='utf-8')
        for pattern in (r'[A-Za-z]:[\\/]+Users[\\/]', r'gh[pousr]_[A-Za-z0-9]{25,}', r'github_pat_[A-Za-z0-9_]{30,}', r'-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----'):
            if re.search(pattern, text):
                errors.append(f'Information privée potentielle : {file.relative_to(ROOT)}')
        if file.suffix == '.md':
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if target.startswith(('https://', 'http://', '#', 'mailto:')):
                    continue
                path = (file.parent / unquote(target.split('#')[0])).resolve()
                if not path.is_relative_to(ROOT) or not path.exists():
                    errors.append(f'Lien local absent : {file.relative_to(ROOT)} -> {target}')

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
print('Liens locaux, inventaires, copie du profil et contrôle de publication : OK')
