#!/usr/bin/env python3
"""Deterministic evidence verification for openline-rsi.

Reads site/data/manifest.json, hashes every copied evidence object, and
fails (nonzero exit) if any bytes no longer match the declared digest.

External references are checked structurally: they must carry a stated
limitation, because their bytes are not locally frozen.

Usage: python3 tools/verify_evidence.py   (run from the repo root)
"""
import hashlib
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    manifest_path = os.path.join(ROOT, "site", "data", "manifest.json")
    try:
        manifest = json.load(open(manifest_path))
    except (OSError, json.JSONDecodeError) as e:
        print(f"FAIL: cannot read manifest: {e}")
        return 1

    failures = []

    for entry in manifest.get("copies", []):
        copy_path = os.path.join(ROOT, entry["copy_path"])
        declared = entry.get("sha256", "")
        if not os.path.isfile(copy_path):
            failures.append(f"missing copy: {entry['copy_path']}")
            continue
        actual = sha256_of(copy_path)
        if actual != declared:
            failures.append(
                f"digest mismatch: {entry['copy_path']}\n"
                f"  declared: {declared}\n"
                f"  actual:   {actual}"
            )
        else:
            print(f"ok  {entry['copy_path']}  {actual[:12]}...")

    for ext in manifest.get("external_references", []):
        if not ext.get("limitation"):
            failures.append(
                f"external reference '{ext.get('key')}' has no stated limitation"
            )
        else:
            print(f"ok  external:{ext.get('key')}  (limitation stated)")

    if failures:
        print("\nFAILURES:")
        for f in failures:
            print(" -", f)
        return 1

    n = len(manifest.get("copies", []))
    print(f"\nverified {n} copied evidence objects; digests match.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
