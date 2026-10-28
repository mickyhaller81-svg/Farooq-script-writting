#!/usr/bin/env python3
"""Mechanical checks for SPEECH_RULES.md (§1, §2, §3, §5). Usage: check_speech.py FILE [FILE ...]"""
import re
import sys

MIN_WORDS, MAX_WORDS = 6100, 8900
TARGET = (7000, 8000)
MAX_SENTENCE = 30
MAX_PARAGRAPH = 120
WPM = 135

ALLOWED_CAPS = {"I", "A", "O", "OK"}


def check(path):
    text = open(path, encoding="utf-8").read()
    errors, warnings = [], []
    lines = text.splitlines()
    headings = [l for l in lines if l.startswith("## ")]
    body = "\n".join(l for l in lines if not l.startswith("#"))
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]

    words = len(body.split())
    if words < MIN_WORDS or words > MAX_WORDS:
        errors.append(f"word count {words} outside hard range {MIN_WORDS}-{MAX_WORDS}")
    elif not TARGET[0] <= words <= TARGET[1]:
        warnings.append(f"word count {words} outside target {TARGET[0]}-{TARGET[1]}")

    if len(headings) < 10:
        warnings.append(f"only {len(headings)} '## ' headings (expected cold open, sign-on, hard truth, 5-7 movements, turn, sign-off)")

    for n, line in enumerate(lines, 1):
        if line.startswith("#"):
            continue
        for ch, name in (("—", "em dash"), ("–", "en dash"), ("[", "bracket"), ("(", "parenthesis"), ("*", "asterisk"), ("_", "underscore")):
            if ch in line:
                errors.append(f"line {n}: {name}")
        if re.search(r"\d", line):
            errors.append(f"line {n}: digit (write numbers as words)")
        for w in re.findall(r"\b[A-Z]{2,}\b", line):
            if w not in ALLOWED_CAPS:
                errors.append(f"line {n}: all-caps word '{w}'")
        if re.search(r"\b(Dr|Mr|Mrs|Ms|St|etc|vs|e\.g|i\.e)\.", line):
            errors.append(f"line {n}: abbreviation")
        if re.search(r"[\U0001F300-\U0001FAFF☀-➿]", line):
            errors.append(f"line {n}: emoji")

    for i, p in enumerate(paragraphs, 1):
        pw = len(p.split())
        if pw > MAX_PARAGRAPH:
            errors.append(f"paragraph {i} has {pw} words (max {MAX_PARAGRAPH}): {p[:60]!r}")
        if p.count("...") > 1:
            errors.append(f"paragraph {i} has more than one '...': {p[:60]!r}")
        for s in re.split(r"(?<=[.!?])\s+", p.replace("...", "…")):
            sw = len(s.split())
            if sw > MAX_SENTENCE:
                errors.append(f"sentence of {sw} words (max {MAX_SENTENCE}): {s[:70]!r}")

    print(f"== {path}")
    print(f"   words {words} (~{words / WPM:.1f} min at {WPM} wpm), headings {len(headings)}, paragraphs {len(paragraphs)}")
    for w in warnings:
        print(f"   WARN  {w}")
    for e in errors:
        print(f"   FAIL  {e}")
    print("   VERDICT:", "PASS" if not errors else f"FIX ({len(errors)} issues)")
    return not errors


if __name__ == "__main__":
    ok = all([check(p) for p in sys.argv[1:]])
    sys.exit(0 if ok else 1)
