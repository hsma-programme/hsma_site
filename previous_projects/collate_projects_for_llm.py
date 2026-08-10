#!/usr/bin/env python3
"""
collate_projects_for_llm.py

Collates every ``index.qmd`` found under the ``previous_projects/hsma_*``
folders (hsma_1 ... hsma_6, hsma_alumni) into a single markdown file intended
to be pasted or loaded as context for an LLM. Projects in ARCHIVE subfolders
are skipped unless ``--include-archive`` is passed.

The prose of each project is reproduced verbatim. Only the metadata is
reshaped: the Quarto YAML front matter of each page is parsed and re-emitted
as a compact, uniform block of labelled fields, and a lookup index of every
project is written at the top of the file so a model can navigate the corpus
without reading it end to end.

Purely presentational front matter keys (``image``, ``title-block-banner``,
``page-layout``, ``grid``, ``toc``, ``categories`` -- the last being a
duplicate of ``techniques`` + ``areas``) are dropped, as are empty links.

No third-party dependencies: the front matter here is a small, regular subset
of YAML, so it is parsed by the mini-parser below rather than PyYAML.

Usage:
    python collate_projects_for_llm.py [--root DIR] [--output FILE]
                                       [--include-archive]

Defaults:
    --root    the folder this script lives in
    --output  <root>/output/hsma_previous_projects_for_llm.md
"""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent

COHORT_GLOB = "hsma_*"
ARCHIVE_DIR_NAME = "ARCHIVE"

# Front matter keys that only control how Quarto renders the page.
SKIPPED_KEYS = {
    "image",
    "title-block-banner",
    "page-layout",
    "grid",
    "toc",
    "categories",  # always the union of `techniques` and `areas`
}


# --------------------------------------------------------------------------
# Minimal YAML subset parser
# --------------------------------------------------------------------------

KEY_RE = re.compile(r"^([A-Za-z][A-Za-z0-9_\-]*)\s*:(?:\s+(.*?))?\s*$")
BLOCK_SCALAR_RE = re.compile(r"^[|>][+-]?$")


def _indent_of(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _skip_blank(lines: list[str], i: int) -> int:
    while i < len(lines) and not lines[i].strip():
        i += 1
    return i


def _parse_scalar(raw: str | None):
    """Unquote a scalar and normalise empty values to None."""
    if raw is None:
        return None
    s = raw.strip()
    if not s:
        return None
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        s = s[1:-1]
    return s or None


def _read_block_scalar(lines: list[str], i: int, parent_indent: int) -> tuple[str, int]:
    """Read a ``|`` / ``>`` literal block: every following line indented
    further than the owning key, dedented to the block's own margin."""
    block: list[str] = []
    while i < len(lines):
        line = lines[i]
        if line.strip() and _indent_of(line) <= parent_indent:
            break
        block.append(line)
        i += 1
    while block and not block[-1].strip():
        block.pop()
    margin = min(
        (_indent_of(line) for line in block if line.strip()),
        default=0,
    )
    return "\n".join(line[margin:] if line.strip() else "" for line in block), i


def _parse_node(lines: list[str], i: int, indent: int):
    """Parse whatever block starts at or after `lines[i]` at column `indent`."""
    i = _skip_blank(lines, i)
    if i >= len(lines) or _indent_of(lines[i]) < indent:
        return None, i
    stripped = lines[i].lstrip(" ")
    if stripped == "-" or stripped.startswith("- "):
        return _parse_sequence(lines, i, indent)
    return _parse_mapping(lines, i, indent)


def _parse_sequence(lines: list[str], i: int, indent: int) -> tuple[list, int]:
    items: list = []
    while True:
        i = _skip_blank(lines, i)
        if i >= len(lines) or _indent_of(lines[i]) != indent:
            break
        stripped = lines[i].lstrip(" ")
        if not (stripped == "-" or stripped.startswith("- ")):
            break

        if stripped == "-":
            # Item body lives on the following lines.
            value, i = _parse_node(lines, i + 1, indent + 2)
            items.append(value)
            continue

        # Rewrite "- foo" as "  foo" so the item body -- which may continue on
        # subsequent lines at the same column -- parses as an ordinary block.
        # Slicing off exactly the two marker characters preserves alignment.
        lines[i] = " " * (indent + 2) + stripped[2:]
        remainder = lines[i].strip()
        if KEY_RE.match(remainder):
            value, i = _parse_mapping(lines, i, indent + 2)
        else:
            value = _parse_scalar(remainder)
            i += 1
        items.append(value)
    return items, i


def _parse_mapping(lines: list[str], i: int, indent: int) -> tuple[dict, int]:
    mapping: dict = {}
    while True:
        i = _skip_blank(lines, i)
        if i >= len(lines) or _indent_of(lines[i]) != indent:
            break
        match = KEY_RE.match(lines[i].strip())
        if not match:
            break
        key, raw = match.group(1), match.group(2)
        i += 1

        if raw is not None and BLOCK_SCALAR_RE.match(raw):
            text, i = _read_block_scalar(lines, i, indent)
            if raw[0] == ">":
                text = " ".join(text.split())
            mapping[key] = text or None
            continue

        if raw is not None and raw.strip():
            mapping[key] = _parse_scalar(raw)
            continue

        # Bare "key:" -- the value is a nested block. A nested sequence may be
        # indented further, or sit at the key's own column (both are valid YAML
        # and both occur in this repo).
        peek = _skip_blank(lines, i)
        if peek < len(lines):
            peek_indent = _indent_of(lines[peek])
            peek_stripped = lines[peek].lstrip(" ")
            is_item = peek_stripped == "-" or peek_stripped.startswith("- ")
            if peek_indent > indent or (peek_indent == indent and is_item):
                mapping[key], i = _parse_node(lines, i, peek_indent)
                continue
        mapping[key] = None
    return mapping, i


def split_front_matter(text: str) -> tuple[dict, str]:
    """Split a .qmd into (parsed front matter, verbatim body)."""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, text.strip()

    for end, line in enumerate(lines[1:], start=1):
        if line.strip() in ("---", "..."):
            meta, _ = _parse_mapping(lines[1:end], 0, 0)
            return meta, "\n".join(lines[end + 1 :]).strip()

    return {}, text.strip()


# --------------------------------------------------------------------------
# Project model
# --------------------------------------------------------------------------

PROJECT_ID_RE = re.compile(r"^([Hh]\d+)[_-](\d+)")


def _as_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return [v for v in value if v not in (None, "")]
    return [value]


def cohort_label(folder_name: str) -> str:
    """'hsma_6' -> 'HSMA 6'; 'hsma_alumni' -> 'HSMA Alumni'."""
    suffix = folder_name.split("_", 1)[1] if "_" in folder_name else folder_name
    return f"HSMA {suffix if suffix.isdigit() else suffix.replace('_', ' ').title()}"


def cohort_sort_key(folder_name: str) -> tuple[int, str]:
    suffix = folder_name.split("_", 1)[1] if "_" in folder_name else folder_name
    # Numbered cohorts first, in order; named ones (alumni) after.
    return (int(suffix), "") if suffix.isdigit() else (10**6, suffix.lower())


class Project:
    """One project page, with its front matter reshaped for LLM consumption."""

    def __init__(self, qmd_path: Path, root: Path, cohort_dir: Path):
        text = qmd_path.read_text(encoding="utf-8", errors="replace")
        self.meta, self.body = split_front_matter(text)

        self.path = qmd_path
        self.rel_path = qmd_path.relative_to(root.parent).as_posix()
        self.cohort_dir = cohort_dir.name
        self.cohort = cohort_label(cohort_dir.name)
        self.archived = any(
            part.upper() == ARCHIVE_DIR_NAME
            for part in qmd_path.relative_to(cohort_dir).parts
        )

        folder = qmd_path.parent.name
        match = PROJECT_ID_RE.match(folder)
        self.project_id = f"{match.group(1).upper()}-{match.group(2)}" if match else folder
        self.number = int(match.group(2)) if match else 0

        self.title = self.meta.get("title") or folder
        self.techniques = _as_list(self.meta.get("techniques"))
        self.areas = _as_list(self.meta.get("areas"))
        self.organisations = _as_list(self.meta.get("organisations"))
        self.status = self.meta.get("status")
        self.has_repo = str(self.meta.get("repo") or "").strip().upper() in ("Y", "YES", "TRUE")

        self.authors = []
        for author in _as_list(self.meta.get("author")):
            if isinstance(author, dict):
                name = author.get("name")
                if name:
                    self.authors.append((name, author.get("affiliation")))
            elif isinstance(author, str):
                self.authors.append((author, None))

        pub_info = self.meta.get("pub-info") or {}
        if not isinstance(pub_info, dict):
            pub_info = {}
        abstract = pub_info.get("abstract")
        self.abstract = " ".join(abstract.split()) if abstract else None

        self.links = []
        for link in _as_list(pub_info.get("links")):
            if isinstance(link, dict) and link.get("name") and link.get("url"):
                self.links.append((link["name"], link["url"]))

        # Any front matter key not already handled, so nothing is silently lost
        # if the site's schema gains a field later.
        handled = SKIPPED_KEYS | {
            "title", "techniques", "areas", "organisations", "status", "repo",
            "author", "pub-info",
        }
        self.extra = {
            k: v
            for k, v in self.meta.items()
            if k not in handled and isinstance(v, (str, int, float))
        }

    @property
    def sort_key(self):
        return cohort_sort_key(self.cohort_dir) + (self.number, self.project_id)

    def author_summary(self) -> str:
        if not self.authors:
            return "Not recorded"
        return "; ".join(
            f"{name} ({affiliation})" if affiliation else name
            for name, affiliation in self.authors
        )

    def to_markdown(self) -> str:
        out = [f"## {self.project_id} — {self.title}", ""]

        fields: list[tuple[str, str]] = [
            ("Project ID", self.project_id),
            ("Cohort", self.cohort),
            ("Authors", self.author_summary()),
            ("Organisations", ", ".join(self.organisations) or "Not recorded"),
            ("Techniques", ", ".join(self.techniques) or "Not recorded"),
            ("Application areas", ", ".join(self.areas) or "Not recorded"),
        ]
        if self.status:
            fields.append(("Status", self.status))
        fields.append(("Public code repository", "Yes" if self.has_repo else "No"))
        if self.archived:
            fields.append(("Listing", "Archived (kept on the site, not in the main listing)"))
        for key, value in self.extra.items():
            fields.append((key, str(value)))
        fields.append(("Source file", self.rel_path))

        out += [f"- **{label}:** {value}" for label, value in fields]

        if self.links:
            out += ["- **Links:**"]
            out += [f"    - {name}: {url}" for name, url in self.links]

        if self.abstract:
            out += ["", "### Abstract", "", self.abstract]

        out += ["", "### Project description", ""]
        out += [self.body if self.body else "_No description text on this page._"]
        return "\n".join(out).rstrip() + "\n"


# --------------------------------------------------------------------------
# Collation
# --------------------------------------------------------------------------


def collect_projects(root: Path, include_archive: bool) -> list[Project]:
    projects = []
    for cohort_dir in sorted(root.glob(COHORT_GLOB)):
        if not cohort_dir.is_dir():
            continue
        for qmd in sorted(cohort_dir.rglob("index.qmd")):
            project = Project(qmd, root, cohort_dir)
            if project.archived and not include_archive:
                continue
            projects.append(project)
    return sorted(projects, key=lambda p: p.sort_key)


def build_header(projects: list[Project], root: Path, include_archive: bool) -> str:
    cohorts: dict[str, int] = {}
    for project in projects:
        cohorts[project.cohort] = cohorts.get(project.cohort, 0) + 1
    cohort_summary = ", ".join(f"{name} ({n})" for name, n in cohorts.items())

    archive_note = (
        "Archived projects are included and flagged with a `Listing` field."
        if include_archive
        else "Projects the site keeps in an ARCHIVE folder are excluded from "
        "this file, so it reflects the main project listing."
    )

    lines = [
        "# HSMA previous projects — full collated corpus",
        "",
        f"- **Generated:** {date.today().isoformat()} "
        f"by `previous_projects/collate_projects_for_llm.py`",
        f"- **Source:** every `index.qmd` under `{root.name}/{COHORT_GLOB}/` "
        "in the HSMA website repository (<https://github.com/hsma-programme/hsma_site>)",
        f"- **Projects in this file:** {len(projects)}",
        f"- **Cohorts:** {cohort_summary}",
        "",
        "## About this document",
        "",
        "HSMA (Health Service Modelling Associates) is a training programme in which "
        "health, social care and policing staff learn simulation, machine learning and "
        "operational research techniques and apply them to a real problem in their own "
        "organisation. Each entry below is one such project.",
        "",
        "## How this document is structured",
        "",
        "- Each project is a level-2 heading of the form "
        "`## <Project ID> — <Title>`, and projects are separated by a horizontal rule.",
        "- Project IDs encode the cohort and project number, e.g. `H6-6015` is "
        "project 6015 from HSMA 6. They are stable and can be cited.",
        "- Under each heading is a bulleted metadata block, then the project's "
        "**Abstract** (a short summary written for the website listing), then the "
        "**Project description** (the full page text).",
        "- Abstract and description text is reproduced verbatim from the source "
        "pages, including any British spellings and Quarto shortcodes such as "
        "`{{< video ... >}}`. Only the metadata has been reformatted.",
        "- `Techniques` and `Application areas` come from a controlled vocabulary "
        "used across the site, so they are reliable for filtering and grouping.",
        f"- {archive_note}",
        "- An index of every project follows; the full entries begin after it.",
        "",
        "## Project index",
        "",
        "| Project ID | Cohort | Title | Techniques | Application areas |",
        "| --- | --- | --- | --- | --- |",
    ]

    for project in projects:
        title = project.title.replace("|", "\\|")
        lines.append(
            f"| {project.project_id} | {project.cohort} | {title} "
            f"| {', '.join(project.techniques)} | {', '.join(project.areas)} |"
        )

    lines += ["", "---", "", "# Projects", ""]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Collate all HSMA previous-project pages into one "
        "LLM-friendly markdown file."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=SCRIPT_DIR,
        help="Folder containing the hsma_* cohort folders "
        "(default: the folder this script lives in).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output file (default: <root>/output/hsma_previous_projects_for_llm.md).",
    )
    parser.add_argument(
        "--include-archive",
        action="store_true",
        help="Also include projects that live in an ARCHIVE subfolder "
        "(they are skipped by default).",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    output = args.output or (root / "output" / "hsma_previous_projects_for_llm.md")
    include_archive = args.include_archive

    projects = collect_projects(root, include_archive)
    if not projects:
        raise SystemExit(f"No index.qmd files found under {root / COHORT_GLOB}")

    document = build_header(projects, root, include_archive) + "\n\n---\n\n".join(
        project.to_markdown() for project in projects
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(document.rstrip() + "\n", encoding="utf-8")

    archived = sum(1 for p in projects if p.archived)
    print(
        f"Wrote {len(projects)} project(s) "
        f"({archived} archived) to {output} "
        f"[{len(document):,} characters, roughly {len(document) // 4:,} tokens]"
    )


if __name__ == "__main__":
    main()
