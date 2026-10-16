#!/usr/bin/env python3
"""Verify selected evidence and replay retained scientific checks offline.

Replays use a disposable copy. No engine, Duck job, service, network request or
installation is started. The omitted global research corpus has a digest-only
provenance check, explicitly distinct from checking its database bytes.
"""
from pathlib import Path, PurePosixPath
import argparse
import ast
import contextlib
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PHYSICAL = Path("GEN4/voli_chapter2_physical3_20261015")
FIELD = Path("GEN4/voli_chapter3_source_field1_20261015")
ORIGINAL_CYCLE_SHA256 = "7368d08ba991e5fbef6ae8e8a52e48dd7ce7df18da0066c055cbb56bd37181e0"

def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def read(path):
    return json.loads(Path(path).read_text())

def verify_manifest(evidence=None):
    evidence = Path(evidence or ROOT / "evidence").resolve()
    manifest = evidence / "MANIFEST.json"
    if manifest.is_symlink() or not manifest.is_file():
        raise ValueError("Evidence manifest must be a regular file")
    d = read(manifest)
    if (not isinstance(d, dict) or d.get("schema") != "SAM_CH2_SELECTED_MANIFEST_V1"
            or not isinstance(d.get("files"), list) or not d["files"]):
        raise ValueError("Unsupported selected evidence manifest")
    seen = set(); total = 0
    for row in d["files"]:
        if not isinstance(row, dict) or not isinstance(row.get("path"), str):
            raise ValueError("Invalid evidence manifest member")
        name = row["path"]; p = PurePosixPath(name)
        if (p.is_absolute() or ".." in p.parts or name in seen or not p.parts
                or "\\" in name or "\0" in name or name != p.as_posix()):
            raise ValueError("Unsafe, noncanonical or duplicate evidence path: " + name)
        if (not isinstance(row.get("sha256"), str) or not re.fullmatch(r"[0-9a-f]{64}", row["sha256"])
                or type(row.get("bytes")) is not int or row["bytes"] < 0):
            raise ValueError("Invalid evidence digest or byte count: " + name)
        path = evidence.joinpath(*p.parts)
        if path.is_symlink() or not path.resolve().is_relative_to(evidence) or not path.is_file():
            raise ValueError("Missing or escaping evidence member: " + name)
        if path.stat().st_size != row["bytes"] or sha(path) != row["sha256"]:
            raise ValueError("Evidence SHA-256/byte count differs: " + name)
        seen.add(name); total += row["bytes"]
    entries = list(evidence.rglob("*"))
    if any(p.is_symlink() for p in entries):
        raise ValueError("Selected evidence contains a symbolic link")
    actual = {str(p.relative_to(evidence)) for p in entries if p.is_file() and p != manifest}
    if actual != seen:
        raise ValueError("Selected evidence file set differs")
    return {"status": "PASS", "files": len(seen), "bytes": total, "manifest_sha256": sha(manifest)}

def adapted_cycle(stage):
    path = stage / PHYSICAL / "verify_cycle.py"
    if sha(path) != ORIGINAL_CYCLE_SHA256:
        raise ValueError("Original physical cycle checker differs")
    run = stage / "GEN4/duck_gen6_local/runs/chapter2-physical-protocols-20261015-01"
    config = read(run / "CONFIG.json")
    expected = config["research"]["index_sha256"]
    original_manifest = stage / "metadata/physical/MANIFEST.sha256"
    old = {}
    for line in original_manifest.read_text().splitlines():
        value, name = line.split("  ", 1)
        old[name] = value
    index_path = str(PHYSICAL / "inputs/RESEARCH_WEB.sqlite")
    if old.get(index_path) != expected:
        raise ValueError("Launch and original archive research-index digests differ")
    old_call = ast.parse("ok('immutable source index '+key,x['returned']['index_sha256']==sha(BASE/'inputs/RESEARCH_WEB.sqlite'))").body[0].value
    old_dump = ast.dump(old_call, include_attributes=False)
    new_call = ast.parse("ok('retained index digest agrees with launch contract; corpus bytes not exported '+key,x['returned']['index_sha256']==portable_index_digest)").body[0].value
    class Replace(ast.NodeTransformer):
        count = 0
        def visit_Call(self, node):
            if ast.dump(node, include_attributes=False) == old_dump:
                self.count += 1
                return ast.copy_location(new_call, node)
            return self.generic_visit(node)
    tree = ast.parse(path.read_text(), filename=str(path)); replacement = Replace()
    tree = ast.fix_missing_locations(replacement.visit(tree))
    if replacement.count != 1:
        raise ValueError("Expected exactly one corpus-byte predicate in original cycle checker")
    namespace = {"__name__": "__main__", "__file__": str(path), "portable_index_digest": expected}
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        exec(compile(tree, str(path), "exec"), namespace)
    return {"source_path": str(PHYSICAL / "verify_cycle.py"), "source_sha256": ORIGINAL_CYCLE_SHA256,
            "ast_predicates_adapted": 1, "index_digest": expected,
            "legacy_cycle_index_bytes_checked": False, "stdout": output.getvalue(),
            "scope": "Only corpus-byte equality is replaced by launch-contract/original-manifest/used-receipt digest agreement; all remaining original predicates execute"}

def execute(stage, script, *args):
    result = subprocess.run([sys.executable, "-B", str(stage / script), *args], cwd=stage,
                            capture_output=True, text=True, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    row = {"script": str(script), "arguments": list(args), "returncode": result.returncode,
           "stdout": result.stdout, "stderr": result.stderr}
    if result.returncode:
        raise RuntimeError("Offline checker failed: " + str(script) + "\n" + result.stdout + result.stderr)
    return row

def replay(stage):
    rows = []
    physical_scripts = ["verify_protocols.py", "closure/verify_source_law.py", "closure/exact_lumped_upper_bound.py",
                        "closure/finalize_closure.py", "closure/verify_cache_semantics.py", "packaging/verify_domain_provenance.py", "verify_native.py"]
    for name in physical_scripts:
        args = ["--require54"] if name == "closure/finalize_closure.py" else []
        rows.append(execute(stage, PHYSICAL / name, *args))
    adaptation = adapted_cycle(stage)
    rows.append({"script": str(PHYSICAL / "verify_cycle.py"), "returncode": 0, "adaptation": adaptation})
    rows.append(execute(stage, FIELD / "reproduce.py", "--skip-manifest"))
    field = read(stage / FIELD / "REPRODUCTION.json")
    counts = {
        "physical_source_law_assertions": read(stage / PHYSICAL / "closure/SOURCE_LAW_VERIFICATION.json")["independent_exact_rational_checks"],
        "physical_point_certificate_assertions": read(stage / PHYSICAL / "closure/FINAL_CLOSURE.json")["independent_point_certificate_checks"],
        "physical_cache_overlap_assertions": read(stage / PHYSICAL / "closure/CACHE_SEMANTICS_VERIFICATION.json")["independent_exact_interval_overlap_checks"],
        "physical_compact_certificate_assertions": read(stage / PHYSICAL / "PROTOCOLS_VERIFICATION.json")["checks_passed"],
        "physical_measurement_assertions": read(stage / PHYSICAL / "measurement/RESULTS.json")["checks_passed"],
        "physical_protocol_assertions": read(stage / PHYSICAL / "protocol/RESULTS.json")["checks_passed"],
        "source_field_assertions": field["independent_science_assertions"],
    }
    native = read(stage / PHYSICAL / "NATIVE_VERIFICATION.json")
    fnative = read(stage / FIELD / "NATIVE_VERIFICATION.json")
    domain = read(stage / PHYSICAL / "packaging/DOMAIN_PROVENANCE_VERIFICATION.json")
    return {"scripts": rows, "scientific_assertions_by_report": counts,
            "scientific_assertions": sum(counts.values()),
            "retained_native_outputs_verified": native["native_outputs_verified"] + fnative["native_outputs_verified"],
            "native_readback_checks": native["independent_checks"] + fnative["independent_checks"],
            "source_domain_returned_calls_authenticated": domain["returned_calls"],
            "source_domain_evaluations_authenticated": domain["returned_source_evaluations"],
            "source_domain_minor_inverses_authenticated": domain["native_source_minor_inverses"],
            "research_receipts_authenticated": fnative["research_receipts_authenticated"] + read(stage / PHYSICAL / "CYCLE_VERIFICATION.json")["research_returns"],
            "portable_adaptations": [adaptation], "legacy_cycle_index_bytes_checked": False}

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--integrity-only", action="store_true")
    ap.add_argument("--output", type=Path, default=ROOT / "build/native_verification.json")
    ap.add_argument("--evidence", type=Path, default=ROOT / "evidence")
    args = ap.parse_args()
    report = {"schema": "SAM_CH2_REPOSITORY_OFFLINE_REPLAY_V1", "status": "RUNNING", "native_executions": 0,
              "network_requests": 0, "runtime_installations": 0}
    try:
        report["initial_evidence_integrity"] = verify_manifest(args.evidence)
        if not args.integrity_only:
            with tempfile.TemporaryDirectory(prefix="sam-ch2-offline-") as folder:
                stage = Path(folder) / "project"
                shutil.copytree(args.evidence, stage)
                report.update(replay(stage))
            report["evidence_integrity_after_replay"] = verify_manifest(args.evidence)
        report["status"] = "INTEGRITY_PASS" if args.integrity_only else "PASS"
    except Exception as error:
        report["status"] = "FAIL"; report["error"] = str(error)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k not in {"scripts", "portable_adaptations"}}))
    if report["status"] == "FAIL":
        raise SystemExit(1)

if __name__ == "__main__":
    main()
