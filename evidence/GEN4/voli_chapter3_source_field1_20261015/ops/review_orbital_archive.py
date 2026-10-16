#!/usr/bin/env python3
"""Authenticate the restored T500 breadcrumb; no science or remote access."""
from pathlib import Path
import hashlib
import json
import tarfile

BASE = Path(__file__).resolve().parents[1]
ARCHIVE = Path('/home/lilhelper/SAM_Research_Overflow/Restored_Research_Data/electron_orbitals_20261015')
receipt = ARCHIVE / 'RESTORATION_RECEIPT.json'
original = json.loads(receipt.read_text())
assert original['status'] == 'PASS'
records = []
for record in original['files']:
    path = Path(record['destination'])
    assert path.resolve().is_relative_to(ARCHIVE.resolve())
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1048576), b''):
            digest.update(chunk)
    assert digest.hexdigest() == record['sha256']
    assert path.stat().st_size == record['bytes']
    records.append(dict(path=str(path), sha256=digest.hexdigest(), bytes=path.stat().st_size))
with tarfile.open(ARCHIVE / 'archives/volii_electron_basis_pod1_20261009_completed_v1.tar.gz', 'r:gz') as archive:
    report = archive.extractfile('volii_electron_basis_pod1/REPORT.md').read()
    members = len(archive.getmembers())
result = dict(
    schema='SAM_CH3_T500_ORBITAL_BREADCRUMB_REVIEW_V1', status='PASS',
    scope='Local restored archive source review; not an operand of the completed chapter cycle.',
    restoration_receipt=dict(path=str(receipt), sha256=hashlib.sha256(receipt.read_bytes()).hexdigest()),
    restored_files_verified=len(records), files=records,
    completed_archive=dict(members=members, report_member='volii_electron_basis_pod1/REPORT.md',
                           report_sha256=hashlib.sha256(report).hexdigest()),
    useful_transfer='Original angular/radial orbital, full massive kinetic, direct/exchange and collective recoil operands for subsequent local energy/stress accounting.',
    original_sources=['He4_4', 'C12_444', 'O16_K4'],
    distinct_missing_source='This electron campaign does not recover the separate Si29 NPZ/coordinate files.',
    portable_replay_dependency=False, native_executions=0, network_requests=0,
    remote_host_access=False, scientific_recalculation=False)
(BASE / 'inputs/ORBITAL_ARCHIVE_REVIEW.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
print('PASS: nine local orbital files and retained report authenticated; follow-up breadcrumb only.')
