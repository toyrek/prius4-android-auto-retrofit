"""Read-only comparison with the project's recorded file hashes. Python 3.9+."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath

DATA = Path(__file__).resolve().parents[1] / 'data'
IGNORED_ROOT_DIRS = {'system volume information', '$recycle.bin'}


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def verify(root, entries, check_extra=True):
    """Return findings; never modify the input tree or follow links outside it."""
    root = Path(root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError('La cible doit être un dossier ou la racine de la clé.')
    expected, issues = set(), []
    for entry in entries:
        rel = entry['path']
        pure = PurePosixPath(rel)
        if pure.is_absolute() or '..' in pure.parts or ':' in rel or '\\' in rel:
            raise ValueError('Chemin non relatif ou dangereux dans le manifeste.')
        if rel in expected:
            raise ValueError('Chemin en double dans le manifeste.')
        expected.add(rel)
        path = root.joinpath(*pure.parts)
        if not path.resolve().is_relative_to(root):
            raise ValueError('Un chemin sort du dossier contrôlé.')
        if not path.is_file():
            issues.append(('MANQUANT', rel))
            continue
        try:
            if path.stat().st_size != entry['bytes']:
                issues.append(('TAILLE', rel))
            elif sha256(path) != entry['sha256']:
                issues.append(('SHA256', rel))
        except OSError as exc:
            issues.append(('LECTURE', f'{rel}: {exc.strerror}'))
    if check_extra:
        def walk(directory):
            for path in directory.iterdir():
                if directory == root and path.name.lower() in IGNORED_ROOT_DIRS and path.is_dir():
                    continue
                rel = path.relative_to(root).as_posix()
                # A link/junction has no place in a firmware USB inventory.
                if path.is_symlink() or (hasattr(path, 'is_junction') and path.is_junction()):
                    issues.append(('LIEN', rel))
                elif path.is_dir():
                    walk(path)
                elif rel not in expected:
                    issues.append(('SUPPLEMENTAIRE', rel))
        walk(root)
    return issues


def main():
    parser = argparse.ArgumentParser(description='Contrôle SHA-256 en lecture seule. Aucun formatage ni flash.')
    parser.add_argument('kind', choices=['archives', 'usb1', 'usb2', 'usb3', 'audio1046'])
    parser.add_argument('directory', type=Path)
    args = parser.parse_args()
    if args.kind == 'archives':
        archive_data = json.loads((DATA / 'downloads.json').read_text(encoding='utf-8'))['archives']
        entries = [dict(path=x['filename'], bytes=x['bytes'], sha256=x['sha256']) for x in archive_data]
    else:
        entries = json.loads((DATA / f'{args.kind}-files.json').read_text(encoding='utf-8'))['files']
    print(f'Lecture de {len(entries)} fichiers attendus. Les grosses clés peuvent prendre plusieurs minutes.', flush=True)
    try:
        issues = verify(args.directory, entries, check_extra=args.kind != 'archives')
    except (ValueError, OSError) as exc:
        print(f'Contrôle interrompu : {exc}')
        return 2
    for status, path in issues:
        print(f'{status}: {path}')
    if issues:
        print(f'NON CONFORME : {len(issues)} écart(s). Ne pas utiliser cette clé comme validée.')
        return 1
    print('CONFORME aux fichiers enregistrés par le projet.')
    print('Ce contrôle ne certifie ni FAT32, ni la compatibilité véhicule, ni une signature Toyota.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
