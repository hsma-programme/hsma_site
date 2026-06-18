#!/usr/bin/env python3
"""
combine_qmd_files.py

Walks each top-level folder in a given root directory (e.g. hsma_1, hsma_2,
hsma_alumni, ...) and concatenates the contents of every .qmd file found
within that folder (recursively, including subfolders like ARCHIVE) into a
single combined markdown file per top-level folder.

Each entry is preceded by a markdown-style comment header containing the
file's path relative to the root, acting as a delimiter between entries.

Usage:
    python combine_qmd_files.py [root_dir] [output_dir]

Defaults:
    root_dir   = the folder this script lives in
    output_dir = an "output" folder inside root_dir
"""

import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent

ARCHIVE_DIR_NAME = "ARCHIVE"


def is_under_archive(path: Path, folder: Path) -> bool:
    """Check whether `path` lies inside an ARCHIVE folder, relative to
    `folder` (case-insensitive match on the directory name)."""
    return any(
        part.upper() == ARCHIVE_DIR_NAME for part in path.relative_to(folder).parts
    )


def find_top_level_folders(root: Path, output_dir: Path) -> list[Path]:
    """Return all top-level subdirectories of root that contain at least
    one .qmd file somewhere within them (recursively), excluding files
    that live only inside ARCHIVE folders, and excluding the output
    directory itself."""
    folders = []
    for entry in sorted(root.iterdir()):
        if entry.resolve() == output_dir.resolve():
            continue
        if entry.is_dir() and any(
            not is_under_archive(qmd, entry) for qmd in entry.rglob("*.qmd")
        ):
            folders.append(entry)
    return folders


def combine_folder_qmds(folder: Path, root: Path) -> str:
    """Find all .qmd files under `folder` (recursively, excluding any
    ARCHIVE subfolders), sort them for deterministic output, and
    concatenate their contents with a delimiter header showing each
    file's path relative to `root`."""
    qmd_files = sorted(
        qmd for qmd in folder.rglob("*.qmd") if not is_under_archive(qmd, folder)
    )

    parts = []
    for qmd_file in qmd_files:
        rel_path = qmd_file.relative_to(root)
        try:
            content = qmd_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = qmd_file.read_text(encoding="utf-8", errors="replace")

        header = f"<!-- ===== {rel_path.as_posix()} ===== -->"
        parts.append(f"{header}\n\n{content.rstrip()}\n")

    return "\n\n".join(parts) + "\n"


def main():
    root_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else SCRIPT_DIR
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else (SCRIPT_DIR / "output")

    root_dir = root_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    top_level_folders = find_top_level_folders(root_dir, output_dir)

    if not top_level_folders:
        print(f"No top-level folders containing .qmd files found under {root_dir}")
        return

    for folder in top_level_folders:
        combined_text = combine_folder_qmds(folder, root_dir)
        out_file = output_dir / f"{folder.name}_combined.md"
        out_file.write_text(combined_text, encoding="utf-8")

        num_files = sum(
            1 for qmd in folder.rglob("*.qmd") if not is_under_archive(qmd, folder)
        )
        print(f"{folder.name}: combined {num_files} .qmd file(s) -> {out_file}")


if __name__ == "__main__":
    main()
