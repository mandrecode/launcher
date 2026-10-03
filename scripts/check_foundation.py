#!/usr/bin/env python3
"""Validate portable Phase 0 contracts; no network or repository mutations."""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]


def local_link_errors(root: Path) -> list[str]:
    errors = []
    paths = [root / 'README.md', root / 'AGENTS.md']
    for directory in ('docs', 'openspec', '.github'):
        paths.extend((root / directory).rglob('*.md'))
    for path in paths:
        if not path.is_file():
            continue
        content = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', content):
            target = target.strip().strip('<>')
            parsed = urlparse(target)
            if parsed.scheme or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            if not resolved.is_relative_to(root.resolve()):
                errors.append(f'{path.relative_to(root)}: link escapes repository: {target}')
            elif not resolved.exists():
                errors.append(f'{path.relative_to(root)}: missing link: {target}')
    return errors


def roadmap_errors(path: Path) -> list[str]:
    with path.open(newline='') as handle:
        rows = list(csv.DictReader(handle))
    ids = [r['id'] for r in rows]
    errors = []
    if len(ids) != len(set(ids)):
        errors.append('Roadmap contains duplicate capability IDs')
    if not rows or any(not re.fullmatch(r'F\d{3}', i) for i in ids):
        errors.append('Roadmap contains missing/invalid capability IDs')
    if any(r['product_status'] != 'planned-not-implemented' for r in rows):
        errors.append('Phase 0 roadmap must not claim implemented behavior')
    return errors


def provenance_errors(lock: dict, reference: dict) -> list[str]:
    errors = []
    if lock['android_release'] != reference['android_release']:
        errors.append('Pixel reference Android release differs from Launcher3 baseline')
    if lock['status'] != 'candidate-not-imported':
        errors.append('Phase 0 source pins must be candidate-not-imported')
    sources = lock.get('sources', [])
    if {s['name'] for s in sources} != {'launcher3', 'systemui-support'}:
        errors.append('Source pin inventory is incomplete')
    for source in sources:
        if not re.fullmatch(r'[0-9a-f]{40}', source['revision']):
            errors.append(f"Invalid immutable source revision: {source['name']}")
        if source['archive_sha256'] is not None:
            errors.append('Phase 0 must not claim an unverified archive digest')
    launcher = next((s for s in sources if s['name'] == 'launcher3'), {})
    if launcher.get('revision') != reference['launcher3_revision']:
        errors.append('Pixel reference source revision differs from source lock')
    return errors


def publication_errors(root: Path) -> list[str]:
    errors = []
    candidates = [root / 'README.md', root / 'AGENTS.md']
    for directory in ('docs', 'openspec', '.github'):
        candidates.extend((root / directory).rglob('*'))
    for path in candidates:
        if not path.is_file():
            continue
        if path.suffix.lower() in {'.jks', '.keystore', '.pem', '.key', '.p12'}:
            errors.append(f'Forbidden credential file: {path.relative_to(root)}')
            continue
        if path.suffix.lower() not in {'.md', '.json', '.yaml', '.yml', '.csv'}:
            continue
        content = path.read_text()
        # Baseline guard, not a replacement for human privacy/license review.
        if re.search(r'/Users/|/var/folders/|-----BEGIN .*PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{20,}', content):
            errors.append(f'Potential private/local content: {path.relative_to(root)}')
    return errors


def check(root: Path = ROOT) -> list[str]:
    errors = []
    for required in ('README.md', 'AGENTS.md', 'docs/phase-0-review.md',
                     'docs/architecture/README.md', 'docs/delivery.md',
                     'docs/github/repository-policy.md', '.github/workflows/ci.yml'):
        if not (root / required).is_file():
            errors.append(f'Missing required artifact: {required}')
    errors.extend(local_link_errors(root))
    errors.extend(roadmap_errors(root / 'docs/product/feature-plan.csv'))
    errors.extend(provenance_errors(
        json.loads((root / 'docs/upstream/sources.lock.json').read_text()),
        json.loads((root / 'docs/product/reference-bundle.template.json').read_text()),
    ))
    errors.extend(publication_errors(root))
    return errors


if __name__ == '__main__':
    failures = check()
    if failures:
        print('\n'.join(f'ERROR: {failure}' for failure in failures))
        raise SystemExit(1)
    print('Foundation checks passed: links, capability IDs/status, source/reference pins and baseline public-content guard.')
