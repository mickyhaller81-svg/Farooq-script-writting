#!/usr/bin/env python3
"""Mechanical checks for HILL_MASTER_BRIEF_3_TOPICS.md, sections 2-4 and 7.

Usage: check_hill.py SCRIPT.txt [--against FILE ...]
--against: other scripts for the 6-gram anti-copy scan (rule 21 / Y1).
"""
import re
import sys

CTA = ("If this is helping you, like the video and leave a comment so the "
       "algorithm can carry it to someone who needs it.")
WPM = 170  # 9,800 words in about 55-60 minutes
FORBIDDEN = [
    (r"\bsubscrib", "subscribe plea"),
    (r"thanks? (you )?for watching", "thanks for watching"),
    (r"\bCarnegie\b", "Carnegie (H6: only as 'Hill told the story that')"),
    (r"five hundred (millionaires|of the richest|successful)", "500 millionaires (H6)"),
    (r"\bWilson\b|\bRoosevelt\b|\bFDR\b", "Wilson/FDR (H6)"),
    (r"\bEdison\b", "Edison (H6)"),
    (r"\bI,? Napoleon Hill\b", "Hill in first person (H2)"),
    (r"here'?s what you'?ll learn|in this video", "table of contents / meta (rule 10)"),
    (r"before it'?s deleted|tell no one", "fake urgency (Y4)"),
    (r"you will be rich|guarantee", "guaranteed result (Y4)"),
    (r"\[|\]", "tag or bracket (rule 15)"),
]
LABEL = re.compile(r"^[^.?!]{1,40}[.?!]$")


def sentences(text):
    t = text.replace("...", "…")
    return [s for s in re.split(r"(?<=[.!?…])[\"”']?\s+", t) if s.strip()]


def words(s):
    return re.findall(r"[A-Za-z']+", s)


def ngrams(text, n=6):
    w = [x.lower() for x in words(text)]
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def check(path, against):
    text = open(path, encoding="utf-8").read().strip()
    errors, info = [], []
    allw = words(text)
    n = len(allw)
    info.append(f"words {n} (~{n / WPM:.0f} min at {WPM} wpm; target ~9,800)")
    if not 9000 <= n <= 10600:
        errors.append(f"word count {n} not near 9,800 (9,000-10,600 accepted)")

    if re.search(r"\d", text):
        errors.append("digits found: " + ", ".join(sorted(set(re.findall(r"\S*\d\S*", text)))[:10]))

    sents = sentences(text)
    lens = [len(words(s)) for s in sents]
    avg = sum(lens) / len(lens)
    info.append(f"sentences {len(sents)}, avg {avg:.1f} words, max {max(lens)}")
    if not 8 <= avg <= 11:
        errors.append(f"average sentence {avg:.1f} words (8-11)")
    for s, l in zip(sents, lens):
        # The CTA wording is fixed by the brief (23 words), so it is exempt.
        if l > 22 and s.strip() != CTA:
            errors.append(f"sentence of {l} words (max 22): {s[:70]!r}")

    you = sum(1 for w in allw if w.lower() in ("you", "your", "you're", "yours", "yourself", "you've", "you'll", "you'd"))
    per100 = you / n * 100
    q = text.count("?")
    per1000 = q / n * 1000
    info.append(f"you/your {per100:.1f} per 100 words (6-8); questions {per1000:.1f} per 1000 (8-15)")
    if not 6 <= per100 <= 8.5:
        errors.append(f"you/your density {per100:.1f} per 100 (6-8)")
    if not 8 <= per1000 <= 15:
        errors.append(f"question density {per1000:.1f} per 1000 (8-15)")

    first = sents[0]
    if not re.search(r"\byou(r)?\b", first, re.I):
        errors.append(f"sentence one has no 'you': {first!r}")
    if re.search(r"\b(Hill|we|nineteen|eighteen)\b", first, re.I):
        errors.append(f"sentence one names author/year/'we': {first!r}")

    c = text.count(CTA)
    if c != 1:
        errors.append(f"exact CTA line appears {c} times (must be once)")
    else:
        pos = len(words(text[:text.index(CTA)]))
        minute = pos / WPM
        info.append(f"CTA at word {pos} (~minute {minute:.1f})")
        if not 6 <= minute <= 12:
            errors.append(f"CTA at ~minute {minute:.1f} (must be 6-12)")

    for pat, name in FORBIDDEN:
        for m in re.finditer(pat, text, re.I):
            errors.append(f"forbidden: {name}: ...{text[max(0, m.start() - 30):m.end() + 30]!r}...")

    quotes = re.findall(r"[\"“][^\"”]+[\"”]", text)
    info.append(f"quotation-mark spans {len(quotes)} (max 3, verbatim only)")
    if len(quotes) > 3:
        errors.append(f"{len(quotes)} quoted spans (max 3)")
    for qt in quotes:
        if len(words(qt)) > 25:
            errors.append(f"quote over 25 words: {qt[:60]!r}")

    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    labels = [p for p in paras if LABEL.match(p) and len(words(p)) <= 6]
    info.append(f"paragraphs {len(paras)}, spoken labels {len(labels)} (~12): {labels}")
    if not 10 <= len(labels) <= 14:
        errors.append(f"{len(labels)} short label paragraphs (about 12 expected)")
    for p in paras:
        if p in labels:
            continue
        k = len(sentences(p))
        if not 3 <= k <= 6 and p.strip() != CTA:
            errors.append(f"paragraph with {k} sentences (3-6): {p[:60]!r}")

    mine = ngrams(text)
    for other in against:
        # The CTA line is fixed by the brief, so it is exempt from the scan.
        shared = (mine & ngrams(open(other, encoding="utf-8").read())) - ngrams(CTA)
        info.append(f"6-gram vs {other}: {len(shared)} shared")
        if shared:
            errors.append(f"6-grams shared with {other}: {sorted(shared)[:8]}")

    print(f"== {path}")
    for i in info:
        print("   " + i)
    for e in errors:
        print("   FAIL  " + e)
    print("   VERDICT:", "PASS" if not errors else f"FIX ({len(errors)} issues)")
    return not errors


if __name__ == "__main__":
    args = sys.argv[1:]
    against = []
    if "--against" in args:
        i = args.index("--against")
        against = args[i + 1:]
        args = args[:i]
    ok = all([check(p, [a for a in against if a != p]) for p in args])
    sys.exit(0 if ok else 1)
