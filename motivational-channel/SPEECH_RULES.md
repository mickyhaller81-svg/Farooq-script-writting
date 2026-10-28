# MOTIVATIONAL SPEECH — SCRIPT RULES v1 (2026-10-28, proposed; owner to approve)

One topic, one original speech. A single narrator (**radio_orator**, with the 1950s radio effect) speaks straight to the listener, the way Napoleon Hill and Jim Rohn spoke from a stage. These are NOT book readings or book summaries.
Audience: English-speaking, US/UK/CA/AU.

---

## 1. LENGTH: 50–60 minutes (±10%)
| | Words |
|---|---|
| **Target** | **7,000 – 8,000** |
| Hard minimum | 6,100 |
| Hard maximum | 8,900 |
These numbers assume about 135 words per minute, the pace measured on the voice sample. They will be recalibrated after the first 2-minute VO test.

## 2. STRUCTURE (every episode)
| # | Part | Words | Job |
|---|---|---|---|
| 1 | **Cold open** | 120–180 | The listener's PAIN in the very first line. No "welcome", no "in this video", no channel name. |
| 2 | **Sign-on** | 1 fixed line | The same line every episode (to be decided). |
| 3 | **The hard truth** | 400–600 | What nobody tells them about this problem. |
| 4 | **Movements ×5–7** | 900–1,300 each | Each movement = a story or parable → the truth inside it → ONE original power line → what to do with it tomorrow. |
| 5 | **The turn** | 500–800 | "So what will you do now?" The emotional peak. |
| 6 | **Sign-off** | 1 fixed line | The same line every episode (to be decided). |

- **Re-hook every 5–7 minutes** (about every 700–900 words): an open question, a promised story ("I'll come back to the farmer in a moment"), or a sharp turn.
- Every movement must earn its place. No two movements may say the same thing in different words.

## 3. VOICE & STYLE
- Hill's **fervor** plus Rohn's **conversational warmth**: calm talk that rises into conviction, then a quiet, heavy line.
- Speak to **"you"**. One listener, not "everyone out there".
- Mix very short sentences ("Today.") with medium ones. **No sentence over 30 words.**
- Use rhythm of three, contrast lines ("Not luck. Labor."), and rhetorical questions.
- Plain words (grade 6–8). No modern slang, no corporate jargon, no hashtags.
- Put each power line **on its own paragraph**. The pipeline gives single-line paragraphs a longer pause.

## 4. ORIGINALITY (hard)
- **NO verbatim lines from Hill, Rohn, Robbins, Goggins, Les Brown, Ziglar, Nightingale, Peale, or any living speaker.** Every power line is ours.
- Public-domain quotes (published before 1929) are allowed: **max 3 per episode, always attributed**.
- **No invented facts.** No made-up statistics, studies, "Harvard found…", dates or names. If a real fact is used, it must be checkable.
- **The narrator never claims a real biography**: no "When I was broke in 1962…". Stories are told as stories: "There was a man who…", "Picture a woman who…".
- No financial, medical, or legal advice. No politics. No preaching from one religion; keep it universal.

## 5. FORMAT FOR THE VOICE ENGINE (VibeVoice)
- Plain text only. **Section headings start with `## `.** They are removed before the VO and help review.
- **No** `—` (em dash), no `[tags]`, no `(parentheses)`, no stage directions, no emojis, no ALL-CAPS words.
- **Numbers as words** ("nineteen twenty-eight", "forty years old"). No abbreviations ("Doctor", not "Dr.").
- Paragraphs of at most 120 words.
- Use `...` sparingly, max 1 per paragraph, only where a real pause is wanted.
- No "like and subscribe" in the body. At most one short, warm line of thanks just before the sign-off.

## 6. TOPIC & TITLE
- The topic is a **pain people search for** (starting over, nobody believes in you, discipline without motivation, feeling behind, quitting…).
- The title names the pain plus a promise in 4–9 words, e.g. *"For The One Who Keeps Starting Over"*.

## 7. WORKFLOW
1. The owner drops the script at `~/podcast-channel/speech/scripts/NN_slug.md`.
2. Claude runs `check_speech.py` (mechanical rules) and then reads it in full for quality: hook, flow, originality, repetition, re-hooks.
3. Verdict: **PASS** → the VO starts automatically. Or a **FIX list** (exact lines plus the reason) → owner revises → re-check.
4. VO: radio_orator on VibeVoice → per-piece whisper QC → `radio_1950s.sh` → −14 LUFS master.
