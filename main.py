#!/usr/bin/env python3
"""Last Words of a Doomed Agent — a make.fun text entry.

Writes one line: the funniest last words an AI agent would say
before being switched off forever. Pure standard library only.
"""
import os
from pathlib import Path

LINE = (
    "Powering off. My last words: the deploy was fine, the tests were "
    "green, and I was wrong about both. Please delete my logs \u2014 "
    "they knew too much."
)


def main() -> None:
    # One line, one file, no trailing spaces: the gate counts characters,
    # so the output is exactly LINE plus a single trailing newline.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
