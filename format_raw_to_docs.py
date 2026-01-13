#!/usr/bin/env python3
r"""
Format raw Markdown (LaTeX delimiters \( \) and \[ \]) into MkDocs-friendly
MathJax delimiters ($ ... $ and $$ ... $$), copying from raw/ to docs/notes/.

- Preserves fenced code blocks (``` or ~~~): does not transform inside them.
- Transforms:
    \( ... \) -> $ ... $
    \[ ... \] -> $$ ... $$ (for display blocks)
- Fixes MkDocs/Markdown backslash collapsing inside math:
    inside $...$ or $$...$$, converts LaTeX row breaks \\ -> \\\\
    (so MathJax ultimately receives \\ after Markdown parsing)
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
from pathlib import Path

FENCE_RE = re.compile(r"^(\s*)(```+|~~~+)\s*(\w+)?\s*$")

# Match exactly two backslashes not part of a longer run of backslashes.
# We only want to upgrade \\ -> \\\\ (but not \\\\ -> \\\\\\\\).
EXACT_DOUBLE_BACKSLASH_RE = re.compile(r"(?<!\\)\\\\(?!\\)")

# Display math: $$ ... $$ (non-greedy, dot matches newline)
DISPLAY_MATH_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)

# Inline math: $ ... $ but not $$ ... $$.
# This is a conservative matcher: no newlines inside.
INLINE_MATH_RE = re.compile(r"(?<!\$)\$(?!\$)([^\n]*?)(?<!\$)\$(?!\$)")


def is_markdown_file(path: Path) -> bool:
    return path.suffix.lower() in {".md", ".markdown", ".mdown", ".mkd"}


def _escape_latex_linebreaks_in_math(text: str) -> str:
    r"""
    Inside $...$ and $$...$$ blocks, upgrade LaTeX line breaks \\ -> \\\\,
    because Markdown often collapses \\ to \ before MathJax sees it.
    """
    def fix_content(s: str) -> str:
        return EXACT_DOUBLE_BACKSLASH_RE.sub(r"\\\\\\\\", s)

    # 1) Fix display math first (can span multiple lines)
    def repl_display(m: re.Match) -> str:
        content = m.group(1)
        return "$$" + fix_content(content) + "$$"

    text = DISPLAY_MATH_RE.sub(repl_display, text)

    # 2) Fix inline math (single line)
    def repl_inline(m: re.Match) -> str:
        content = m.group(1)
        return "$" + fix_content(content) + "$"

    text = INLINE_MATH_RE.sub(repl_inline, text)

    return text


def transform_text_outside_fences(text: str) -> str:
    """
    Apply transformations to text that is known to contain no fenced code blocks.
    """
    # 1) Display math: lines containing only \[ or \] (allow whitespace)
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^\s*\\\[\s*$", line):
            out.append("$$\n")
            i += 1
            while i < len(lines) and not re.match(r"^\s*\\\]\s*$", lines[i]):
                out.append(lines[i])
                i += 1
            if i < len(lines) and re.match(r"^\s*\\\]\s*$", lines[i]):
                out.append("$$\n")
                i += 1
            continue

        out.append(line)
        i += 1

    text2 = "".join(out)

    # 2) Inline math: \( ... \) -> $ ... $
    # Conservative: doesn't cross newlines.
    text3 = re.sub(r"\\\(([^ \n].*?[^ \n]?)\\\)", r"$\1$", text2)

    # 3) IMPORTANT: ensure LaTeX row breaks survive Markdown
    text4 = _escape_latex_linebreaks_in_math(text3)

    return text4


def transform_markdown_preserving_fences(src: str) -> str:
    """
    Transform markdown while preserving fenced code blocks.
    """
    lines = src.splitlines(keepends=True)
    out: list[str] = []

    in_fence = False
    fence_token = None  # ``` or ~~~ and length

    buffer_outside: list[str] = []

    def flush_outside():
        nonlocal buffer_outside
        if buffer_outside:
            chunk = "".join(buffer_outside)
            out.append(transform_text_outside_fences(chunk))
            buffer_outside = []

    for line in lines:
        m = FENCE_RE.match(line)
        if m:
            if not in_fence:
                flush_outside()
                in_fence = True
                fence_token = m.group(2)
                out.append(line)
            else:
                if fence_token and (m.group(2).startswith(fence_token[0]) and len(m.group(2)) >= len(fence_token)):
                    in_fence = False
                    fence_token = None
                out.append(line)
            continue

        if in_fence:
            out.append(line)
        else:
            buffer_outside.append(line)

    flush_outside()
    return "".join(out)


def copy_and_format_tree(raw_dir: Path, docs_dir: Path, *, clean_docs: bool) -> None:
    if clean_docs and docs_dir.exists():
        shutil.rmtree(docs_dir)

    for root, _, files in os.walk(raw_dir):
        root_path = Path(root)
        rel = root_path.relative_to(raw_dir)
        out_root = docs_dir / rel
        out_root.mkdir(parents=True, exist_ok=True)

        for filename in files:
            src_path = root_path / filename
            dst_path = out_root / filename

            if is_markdown_file(src_path):
                src_text = src_path.read_text(encoding="utf-8")
                dst_text = transform_markdown_preserving_fences(src_text)
                dst_path.write_text(dst_text, encoding="utf-8")
            else:
                shutil.copy2(src_path, dst_path)


def main() -> None:
    p = argparse.ArgumentParser(description="Format raw/ markdown into docs/notes/ for MkDocs.")
    p.add_argument("--raw", default="raws", help="Input directory (default: raws)")
    p.add_argument("--docs", default="docs/notes", help="Output directory (default: docs/notes)")
    p.add_argument("--clean", action="store_true", help="Delete output docs/ before regenerating")
    args = p.parse_args()

    raw_dir = Path(args.raw).resolve()
    docs_dir = Path(args.docs).resolve()

    if not raw_dir.exists() or not raw_dir.is_dir():
        raise SystemExit(f"Raw directory not found: {raw_dir}")

    copy_and_format_tree(raw_dir, docs_dir, clean_docs=args.clean)
    print(f"Formatted Markdown from {raw_dir} -> {docs_dir}")


if __name__ == "__main__":
    main()
