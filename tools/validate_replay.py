#!/usr/bin/env python3
"""Validate the replay data model for openline-rsi.

Enforces the data contract:
  - every earned (frozen) stage binds to evidence (manifest key + sha256);
  - an earned stage with no evidence binding is invalid -> nonzero exit;
  - every future/unearned stage renders explicitly as unresolved, with a
    label and no verdict;
  - there is no schema state that looks complete while no result exists;
  - historical verdict and current standing are separate fields: stage-level
    "standing" keys are rejected; standing lives only in the top-level
    "standing" object.

Usage: python3 tools/validate_replay.py   (run from the repo root)
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHA_RE = re.compile(r"^[0-9a-f]{64}$")


def fail(errors, msg):
    errors.append(msg)


def main():
    errors = []

    replay_path = os.path.join(ROOT, "site", "data", "replay.json")
    contrast_path = os.path.join(ROOT, "site", "data", "contrast.json")
    manifest_path = os.path.join(ROOT, "site", "data", "manifest.json")
    try:
        replay = json.load(open(replay_path))
        contrast = json.load(open(contrast_path))
        manifest = json.load(open(manifest_path))
    except (OSError, json.JSONDecodeError) as e:
        print(f"FAIL: cannot read data: {e}")
        return 1

    manifest_keys = {c["key"]: c for c in manifest.get("copies", [])}
    manifest_keys.update({e["key"]: e for e in manifest.get("external_references", [])})
    manifest_lookup = manifest_keys

    if replay.get("schema") != "openline.rsi.replay.v1":
        fail(errors, "replay.json: unexpected schema value")

    stages = replay.get("stages", [])
    if not stages:
        fail(errors, "replay.json: no stages")

    for i, st in enumerate(stages):
        where = f"stage[{i}] key={st.get('key')!r}"
        status = st.get("status")
        if status not in ("frozen", "unresolved"):
            fail(errors, f"{where}: status must be 'frozen' or 'unresolved', got {status!r}")
            continue
        if "standing" in st:
            fail(errors, f"{where}: stage-level 'standing' is forbidden; "
                         "standing lives only in the top-level 'standing' object")
        plain = st.get("plain", {})
        if not plain.get("headline") or not plain.get("body"):
            fail(errors, f"{where}: plain.headline and plain.body are required")

        if status == "frozen":
            rec = st.get("record")
            if not rec:
                fail(errors, f"{where}: frozen stage has no evidence binding -> INVALID")
                continue
            key = rec.get("evidence_key")
            entry = manifest_lookup.get(key)
            if not entry:
                fail(errors, f"{where}: evidence_key {key!r} not in manifest")
                continue
            if entry.get("verification") == "verified-copy":
                if not SHA_RE.match(entry.get("sha256", "")):
                    fail(errors, f"{where}: manifest entry {key!r} lacks a valid sha256")
                copy_path = os.path.join(ROOT, entry["copy_path"])
                if not os.path.isfile(copy_path):
                    fail(errors, f"{where}: copied evidence missing: {entry['copy_path']}")
            elif entry.get("kind"):
                # external reference: must state its limitation
                if not entry.get("limitation"):
                    fail(errors, f"{where}: external evidence {key!r} has no stated limitation")
            else:
                fail(errors, f"{where}: manifest entry {key!r} has no verification/kind")
        else:  # unresolved
            if st.get("verdict"):
                fail(errors, f"{where}: unresolved stage must not carry a verdict")
            if not st.get("label") and not plain.get("headline"):
                fail(errors, f"{where}: unresolved stage needs an explicit label")

    # future slots: all unresolved, labeled, with a plug-in location
    for slot in replay.get("future_slots", []):
        if slot.get("status") != "unresolved":
            fail(errors, f"future slot {slot.get('key')!r}: must be 'unresolved'")
        if not slot.get("label") or not slot.get("plug_in"):
            fail(errors, f"future slot {slot.get('key')!r}: needs label and plug_in")

    # contrast lane: same contract
    if contrast.get("schema") != "openline.rsi.contrast.v1":
        fail(errors, "contrast.json: unexpected schema value")
    for lane in contrast.get("lanes", []):
        for rec in lane.get("records", []):
            key = rec.get("evidence_key")
            if key not in manifest_lookup:
                fail(errors, f"contrast lane {lane.get('id')!r}: evidence_key {key!r} not in manifest")

    # standing: separate object, dated, entries reference historical verdicts only
    standing = replay.get("standing")
    if not standing or not standing.get("as_of"):
        fail(errors, "replay.json: standing must be a separate, dated object")
    for e in standing.get("entries", []):
        if "historical_verdict" not in e or "current_standing" not in e:
            fail(errors, "replay.json: standing entries need historical_verdict + current_standing")

    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print(" -", e)
        return 1

    print(f"replay valid: {len(stages)} stages, "
          f"{sum(1 for s in stages if s['status']=='frozen')} frozen, "
          f"{sum(1 for s in stages if s['status']=='unresolved')} unresolved, "
          f"{len(replay.get('future_slots', []))} future slots, "
          f"{len(contrast.get('lanes', []))} contrast lanes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
