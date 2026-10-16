"""Portable inventory rejection and public manuscript/source bindings."""
from pathlib import Path
import hashlib
import importlib.util
import json
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('chapter2_assets',ROOT/'scripts/verify_repository.py')
assets=importlib.util.module_from_spec(spec);spec.loader.exec_module(assets)

class AssetTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name);self.file=self.root/'input.txt';self.file.write_bytes(b'signed source')
        self.row=dict(path='input.txt',bytes=self.file.stat().st_size,sha256=hashlib.sha256(self.file.read_bytes()).hexdigest())
    def manifest(self,rows=None):
        (self.root/'MANIFEST.json').write_text(json.dumps(dict(schema='SAM_CHAPTER_II_PORTABLE_ASSETS_V1',files=rows if rows is not None else [self.row])))
    def test_valid_inventory(self):
        self.manifest();self.assertEqual(assets.verify_assets(self.root)['files'],1)
    def test_changed_signed_source_rejected(self):
        self.manifest();self.file.write_bytes(b'changed source')
        with self.assertRaises(ValueError):assets.verify_assets(self.root)
    def test_missing_source_rejected(self):
        self.manifest();self.file.unlink()
        with self.assertRaises(ValueError):assets.verify_assets(self.root)
    def test_duplicate_inventory_rejected(self):
        self.manifest([self.row,self.row])
        with self.assertRaises(ValueError):assets.verify_assets(self.root)
    def test_nonportable_paths_rejected(self):
        for name in ['../input.txt','/input.txt','./input.txt','a//b','a\\b','']:
            with self.subTest(name=name):
                self.manifest([{**self.row,'path':name}])
                with self.assertRaises(ValueError):assets.verify_assets(self.root)
    def test_symlink_asset_rejected(self):
        self.file.rename(self.root/'original.txt');self.file.symlink_to('original.txt');self.manifest()
        with self.assertRaises(ValueError):assets.verify_assets(self.root)
    def test_empty_manifest_rejected(self):
        self.manifest([])
        with self.assertRaises(ValueError):assets.verify_assets(self.root)
    def test_wrong_byte_count_rejected(self):
        self.manifest([{**self.row,'bytes':self.row['bytes']+1}])
        with self.assertRaises(ValueError):assets.verify_assets(self.root)
    def test_reviewed_pdf_and_editable_source_bindings(self):
        provenance=json.loads((ROOT/'data/manuscript_provenance.json').read_text())
        self.assertEqual((provenance['pages'],provenance['sections']),(24,48))
        self.assertEqual(hashlib.sha256((ROOT/'manuscript/Chapter_II.pdf').read_bytes()).hexdigest(),provenance['reviewed_pdf_sha256'])
        for row in provenance['files']:
            self.assertEqual(hashlib.sha256((ROOT/row['path']).read_bytes()).hexdigest(),row['sha256'])

if __name__=='__main__':unittest.main()
