#!/usr/bin/env python3
"""Archive only the requested committed sources, then verify every byte."""

import subprocess
import sys
from pathlib import Path
from zipfile import ZipFile


def git(*args):
    return subprocess.check_output(["git", *args])


def package(output):
    commit = git("rev-parse", "HEAD").decode().strip()
    paths = ["Bao_cao_TTTN.tex", "References.bib", "Regulations.tex", "figures"]
    entries = git("ls-tree", "-rz", commit, "--", *paths).split(b"\0")
    expected = {}
    for entry in filter(None, entries):
        metadata, name = entry.split(b"\t", 1)
        mode, kind, oid = metadata.split()
        if kind != b"blob" or mode not in (b"100644", b"100755"):
            raise ValueError(f"Only regular source files are allowed: {name!r}")
        filename = name.decode("utf-8")
        if any(part in (".git", "..") for part in filename.split("/")):
            raise ValueError(f"Unsafe source path: {filename}")
        expected[filename] = oid.decode()
    if not set(paths[:3]) <= expected.keys():
        raise ValueError("A required committed source file is missing")
    if not any(name.startswith("figures/") for name in expected):
        raise ValueError("No committed files in figures/")

    output = Path(output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["git", "archive", "--format=zip", f"--output={output}", commit, "--", *paths],
        check=True,
    )
    with ZipFile(output) as archive:
        files = [item.filename for item in archive.infolist() if not item.is_dir()]
        if len(files) != len(set(files)) or set(files) != set(expected):
            raise ValueError("Archive contains missing, duplicate, or unexpected files")
        for name, oid in expected.items():
            if archive.read(name) != git("cat-file", "blob", oid):
                raise ValueError(f"Archive differs from the committed source: {name}")
        if archive.testzip() is not None:
            raise ValueError("ZIP CRC validation failed")
    print(f"Verified {len(expected)} source files from {commit} in {output.name}")
    for name in sorted(expected):
        print(f"  {name}")


if __name__ == "__main__":
    package(sys.argv[1] if len(sys.argv) > 1 else ".artifacts/LaTeX-TTTN.zip")
