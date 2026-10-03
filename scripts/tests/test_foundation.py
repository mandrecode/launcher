"""Behavioral regression tests for guards protecting public artifacts."""
import copy
import csv
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / 'check_foundation.py'
spec = importlib.util.spec_from_file_location('foundation', MODULE)
foundation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foundation)


class FoundationGuardsTest(unittest.TestCase):
    def test_local_links_reject_missing_target_and_repository_escape(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'README.md').write_text('[Missing](missing.md) [Escape](../outside.md)')
            errors = foundation.local_link_errors(root)
            self.assertEqual(len(errors), 2)
            self.assertTrue(any('escapes' in e for e in errors))

    def test_remote_and_fragment_links_do_not_require_local_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'README.md').write_text('[Web](https://example.org/x) [Section](#section)')
            self.assertEqual(foundation.local_link_errors(root), [])

    def test_duplicate_roadmap_ids_and_implemented_claims_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'roadmap.csv'
            with path.open('w', newline='') as handle:
                writer = csv.DictWriter(handle, fieldnames=['id', 'product_status'])
                writer.writeheader()
                writer.writerows([{'id': 'F001', 'product_status': 'implemented'},
                                  {'id': 'F001', 'product_status': 'planned-not-implemented'}])
            self.assertEqual(len(foundation.roadmap_errors(path)), 2)

    def test_different_android_reference_release_is_rejected(self):
        root = foundation.ROOT
        lock = json.loads((root / 'docs/upstream/sources.lock.json').read_text())
        reference = json.loads((root / 'docs/product/reference-bundle.template.json').read_text())
        self.assertEqual(foundation.provenance_errors(lock, reference), [])
        other = copy.deepcopy(reference)
        other['android_release'] = '18'
        self.assertTrue(any('release differs' in e for e in foundation.provenance_errors(lock, other)))

    def test_local_private_paths_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'README.md').write_text('Private capture at ' + '/Users/' + 'example/capture.png')
            self.assertEqual(len(foundation.publication_errors(root)), 1)


if __name__ == '__main__':
    unittest.main()
