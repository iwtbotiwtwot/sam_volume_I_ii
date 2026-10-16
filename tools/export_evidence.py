#!/usr/bin/env python3
"""Export a verified, bounded Chapter II evidence subset from two retained ZIPs.

This tool reads only the named archives. It does not run science or contact a
runtime. Original member bytes are retained; corpus databases and runtime bulk
are omitted explicitly and listed in EXPORT.json.
"""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import stat
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ARCHIVES = {
    "physical": ("SAM_Volume_I_Chapter_II_Physical_Development_and_Verification_20261015.zip",
                 "e90115a3e46288338baa079e434a2ddccf9d12edfec230b20b7d4bb631aa90ee"),
    "source_field": ("SAM_Volume_I_Chapters_II_III_Source_to_Field_and_Verification_20261015.zip",
                     "9c0015da9913d0056f62611bd9cf99a3583f477802fc8b6ecc2bf746cd7a9670"),
}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def omitted_reason(name):
    p = PurePosixPath(name)
    if p.suffix == ".sqlite" or ".sqlite." in p.name:
        return "Global research-index corpus; launch digest and used receipts retained"
    if name.startswith("GEN4/duck_dual_session_topology1_20261015/"):
        return "Separate runtime engineering qualification, outside Chapter II science"
    if "/executed_code/" in name and name.startswith("GEN4/duck_gen6_local/"):
        return "Installed runtime/core implementation snapshot; no replacement runtime published"
    if "/ops/authority_preimages/" in name or "/ops/prior_authority/" in name:
        return "Unrelated mutable authority preimages"
    if p.name in {"MONITOR.jsonl", "OPERATOR_VIEW.json"}:
        return "Repeated operational monitoring, not a scientific operand or receipt"
    if any(x in {"R3_STATE", "checkpoints", "runtime", "ram_scratch", ".git", "__pycache__"} for x in p.parts):
        return "Runtime state or bulk cache"
    return None

def load_archive(path, expected):
    raw = path.read_bytes()
    if digest(raw) != expected:
        raise ValueError("Archive SHA-256 differs: " + str(path))
    with zipfile.ZipFile(path) as z:
        infos = z.infolist()
        names = [i.filename for i in infos if not i.is_dir()]
        if len(names) != len(set(names)):
            raise ValueError("Duplicate archive member")
        roots = {PurePosixPath(n).parts[0] for n in names}
        if len(roots) != 1:
            raise ValueError("Archive must have exactly one root")
        prefix = roots.pop() + "/"
        members = {}
        for i in infos:
            if i.is_dir():
                continue
            p = PurePosixPath(i.filename)
            mode = i.external_attr >> 16
            if p.is_absolute() or ".." in p.parts or stat.S_ISLNK(mode):
                raise ValueError("Unsafe archive member: " + i.filename)
            members[i.filename[len(prefix):]] = z.read(i)
    manifest = members["MANIFEST.sha256"].decode()
    listed = {}
    for line in manifest.splitlines():
        sha, name = line.split("  ", 1)
        if name in listed or name not in members:
            raise ValueError("Invalid upstream manifest path: " + name)
        listed[name] = sha
        if digest(members[name]) != sha:
            raise ValueError("Upstream manifest SHA-256 differs: " + name)
    if set(listed) != set(members) - {"MANIFEST.sha256"}:
        raise ValueError("Upstream manifest file set differs")
    return members, {"name": path.name, "sha256": expected, "bytes": len(raw),
                     "members_authenticated": len(members), "manifest_sha256": digest(members["MANIFEST.sha256"])}

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for label, (name, _) in ARCHIVES.items():
        ap.add_argument("--" + label.replace("_", "-") + "-archive", type=Path,
                        default=Path.home() / "Downloads" / name)
    ap.add_argument("--destination", type=Path, default=ROOT / "evidence")
    args = ap.parse_args()
    destination = args.destination.resolve()
    if destination != ROOT / "evidence":
        raise ValueError("Export destination must be this repository's evidence/ directory")
    if destination.exists() and any(destination.iterdir()):
        raise ValueError("Refusing to replace an existing evidence tree")
    destination.mkdir(parents=True, exist_ok=True)
    records = {}; omitted = []; archives = {}
    for label, (_, expected) in ARCHIVES.items():
        members, archives[label] = load_archive(getattr(args, label + "_archive"), expected)
        for original, data in sorted(members.items()):
            reason = omitted_reason(original)
            if reason:
                omitted.append({"archive": label, "path": original, "sha256": digest(data), "bytes": len(data), "reason": reason})
                continue
            target = ("metadata/" + label + "/" + original) if "/" not in original or original.startswith("predecessor_metadata/") else original
            if target in records:
                if records[target]["sha256"] != digest(data):
                    raise ValueError("Conflicting original evidence bytes: " + target)
                records[target]["archives"].append(label)
                continue
            path = destination / target
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            records[target] = {"path": target, "sha256": digest(data), "bytes": len(data),
                               "archives": [label], "original_member": original}
    export = {"schema": "SAM_CH2_SELECTED_EXPORT_V1", "status": "PASS", "archives": archives,
              "selected_original_files": len(records), "selected_original_bytes": sum(r["bytes"] for r in records.values()),
              "omitted_files": omitted, "source_bytes_modified": False,
              "scope": "Selected original scientific operands, derivations, manuscript sources and receipt evidence; no global corpus or installed runtime"}
    data = (json.dumps(export, indent=2, sort_keys=True) + "\n").encode()
    (destination / "EXPORT.json").write_bytes(data)
    records["EXPORT.json"] = {"path": "EXPORT.json", "sha256": digest(data), "bytes": len(data), "role": "Selected-export provenance"}
    manifest = {"schema": "SAM_CH2_SELECTED_MANIFEST_V1", "files": [records[k] for k in sorted(records)]}
    (destination / "MANIFEST.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: export[k] for k in ["status", "selected_original_files", "selected_original_bytes", "source_bytes_modified"]}))

if __name__ == "__main__":
    main()
