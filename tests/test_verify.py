import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('verify', Path(__file__).resolve().parents[1] / 'tools/verify.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class VerifyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'file.kwi').write_bytes(b'abcd')
        self.entries = [dict(path='file.kwi', bytes=4, sha256=hashlib.sha256(b'abcd').hexdigest())]

    def test_match_and_no_mutation(self):
        before = (self.root / 'file.kwi').stat().st_mtime_ns
        self.assertEqual(module.verify(self.root, self.entries), [])
        self.assertEqual((self.root / 'file.kwi').read_bytes(), b'abcd')
        self.assertEqual((self.root / 'file.kwi').stat().st_mtime_ns, before)

    def test_same_size_corruption(self):
        (self.root / 'file.kwi').write_bytes(b'zzzz')
        self.assertEqual(module.verify(self.root, self.entries), [('SHA256', 'file.kwi')])

    def test_wrong_size(self):
        (self.root / 'file.kwi').write_bytes(b'a')
        self.assertEqual(module.verify(self.root, self.entries), [('TAILLE', 'file.kwi')])

    def test_missing_and_extra(self):
        (self.root / 'file.kwi').rename(self.root / 'wrong.kwi')
        self.assertEqual(set(module.verify(self.root, self.entries)), {('MANQUANT', 'file.kwi'), ('SUPPLEMENTAIRE', 'wrong.kwi')})

    def test_system_directory_only_ignored_at_root(self):
        (self.root / 'System Volume Information').mkdir()
        (self.root / 'System Volume Information' / 'test').write_bytes(b'x')
        self.assertEqual(module.verify(self.root, self.entries), [])
        (self.root / 'another').mkdir()
        (self.root / 'another' / 'System Volume Information').mkdir()
        (self.root / 'another' / 'System Volume Information' / 'test').write_bytes(b'x')
        self.assertEqual(module.verify(self.root, self.entries), [('SUPPLEMENTAIRE', 'another/System Volume Information/test')])

    def test_refuse_escaping_manifest(self):
        for path in ('../elsewhere', '/outside', 'C:/outside', 'folder\\file'):
            with self.subTest(path=path), self.assertRaises(ValueError):
                module.verify(self.root, [dict(self.entries[0], path=path)])


if __name__ == '__main__':
    unittest.main()
