"""Selected-evidence integrity and bounded portable adaptation rejection."""
from pathlib import Path
import hashlib
import importlib.util
import json
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('chapter2_native',ROOT/'scripts/verify_native.py')
native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native)

class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name);self.member=self.root/'receipt.json';self.member.write_text('{"signed":-2}')
        self.row=dict(path='receipt.json',bytes=self.member.stat().st_size,sha256=hashlib.sha256(self.member.read_bytes()).hexdigest())
    def manifest(self,rows=None):
        (self.root/'MANIFEST.json').write_text(json.dumps(dict(schema='SAM_CH2_SELECTED_MANIFEST_V1',files=rows if rows is not None else [self.row])))
    def test_valid_selected_inventory(self):
        self.manifest();self.assertEqual(native.verify_manifest(self.root)['files'],1)
    def test_tampered_receipt_rejected(self):
        self.manifest();self.member.write_text('{"signed":+2}')
        with self.assertRaises(ValueError):native.verify_manifest(self.root)
    def test_missing_receipt_rejected(self):
        self.manifest();self.member.unlink()
        with self.assertRaises(ValueError):native.verify_manifest(self.root)
    def test_unlisted_evidence_rejected(self):
        self.manifest();(self.root/'extra.json').write_text('{}')
        with self.assertRaises(ValueError):native.verify_manifest(self.root)
    def test_duplicate_inventory_rejected(self):
        self.manifest([self.row,self.row])
        with self.assertRaises(ValueError):native.verify_manifest(self.root)
    def test_absolute_and_traversal_rejected(self):
        for name in ['../receipt.json','/receipt.json']:
            with self.subTest(name=name):
                self.manifest([{**self.row,'path':name}])
                with self.assertRaises(ValueError):native.verify_manifest(self.root)
    def test_symbolic_receipt_rejected(self):
        self.member.rename(self.root/'original');self.member.symlink_to('original');self.manifest()
        with self.assertRaises(ValueError):native.verify_manifest(self.root)
    def test_wrong_length_rejected(self):
        self.manifest([{**self.row,'bytes':1}])
        with self.assertRaises(ValueError):native.verify_manifest(self.root)
    def test_checker_source_change_rejected_before_adaptation(self):
        original=self.root/native.PHYSICAL/'verify_cycle.py';original.parent.mkdir(parents=True)
        original.write_text('raise AssertionError("altered checker")\n')
        with self.assertRaisesRegex(ValueError,'checker differs'):native.adapted_cycle(self.root)
    def test_public_export_omits_global_corpus_and_runtime(self):
        manifest=json.loads((ROOT/'evidence/MANIFEST.json').read_text())
        self.assertGreater(len(manifest['files']),1000)
        self.assertFalse(any(row['path'].endswith('.sqlite') for row in manifest['files']))
        self.assertFalse(any(row['path'].startswith('GEN4/duck_gen6_local/') and
                             '/executed_code/' in row['path'] for row in manifest['files']))

if __name__=='__main__':unittest.main()
