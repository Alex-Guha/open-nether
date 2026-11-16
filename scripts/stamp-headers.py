#!/usr/bin/env python3
# Open Nether, 2026 (PolyForm Shield License 1.0.0). See NOTICE and LICENSE.
"""Stamp the origin and licence header on every Java source file that has none (LICENSING.md).

    python3 scripts/stamp-headers.py            add our header to every file in src/*/java that starts without a comment
    python3 scripts/stamp-headers.py --check    stamp nothing; report files without a header. Exit status 1 on any

A file written for this mod starts with HEADER below. A file copied from another work keeps that work's header: any
block comment at the top that names a licence ("License" or "Licence") is accepted, so give such a file a line naming
our changes and a row in LICENSING.md's table by hand. Run from the repository root.
"""
import glob
import sys

HEADER = """/*
 * Open Nether, 2026 (PolyForm Shield License 1.0.0). See NOTICE and LICENSE.
 */
"""
OURS = "Open Nether, "


def kind(src):
    """'ours', 'other' (another work's licence header), or None (no header)"""
    head = src.lstrip()[:1200]
    if not head.startswith("/*"):
        return None
    comment = head[:head.find("*/")] if "*/" in head else head
    if OURS in comment and "PolyForm Shield" in comment:
        return "ours"
    if "License" in comment or "Licence" in comment:
        return "other"
    return None


def main():
    files = sorted(glob.glob("src/*/java/**/*.java", recursive=True))
    counts = {"ours": 0, "other": 0, "missing": 0}
    missing = []
    for path in files:
        with open(path, encoding="utf-8") as f:
            src = f.read()
        found = kind(src)
        if found:
            counts[found] += 1
            continue
        counts["missing"] += 1
        missing.append(path)
        if "--check" not in sys.argv[1:]:
            with open(path, "w", encoding="utf-8") as f:
                f.write(HEADER + src)
    if "--check" in sys.argv[1:]:
        print(f"{len(files)} Java files: {counts['ours']} ours, {counts['other']} under another work's header, "
              f"{counts['missing']} without a header")
        for path in missing:
            print("MISSING " + path)
        sys.exit(1 if missing else 0)
    print(f"stamped {len(missing)} file(s)" + "".join("\n  " + p for p in missing))


if __name__ == "__main__":
    main()
