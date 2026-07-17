# Faceless YouTube Cash Machine

A **no-camera, fully-automated YouTube Shorts pipeline** that actually clears
YouTube's quality bar — plus a free in-browser tool you can use right now.

👉 **Live free tool:** https://avi5129.github.io/faceless-cash-machine/
👉 **Full toolkit (paid, $9):** https://avi5129.gumroad.com/l/faceless-cash-machine

---

## What this is

Most "faceless YouTube" advice gets channels demonetized: reused audio, stolen
visuals, missing captions. This pipeline is engineered to defeat all three by
design, built from a real, tested Python engine — not theory.

| Module | Job | Quality spec |
|--------|-----|--------------|
| `script_pro` | Writes 25–40s script, rotates hooks | Hook → payload → CTA; 5 hook variants |
| `voice_pro` | TTS with graceful fallback | Chatterbox→Kokoro→edge-tts→silent; −14 LUFS |
| `visuals_pro` | Finds B-roll | CC0 / CC-BY only, source logged |
| `captions` | Word-level burned subtitles | stable-ts, gold `#F5C518`, safe area |
| `edit_pro` | Assembles the Short | 2.5–4s shots, gold-wipe transition |
| `scheduler` | Queues publishing | 3/day, **human approves publish** |

## Try it free (browser)

The landing page has a working topic + hook generator — no signup, runs in your
browser. [Open it →](https://avi5129.github.io/faceless-cash-machine/)

## Run the toolkit locally

```bash
python bonus/topic_engine.py --niche finance --count 10
python bonus/checklist.py --date 2026-07-19 --count 3
```

Both scripts are **standard library only** — no `pip install` needed.

## What's in the paid bundle

- `guide.html` — the complete pipeline guide (voice chain, loudness, captions, visuals, edit rhythm, monetization).
- `PREMIUM.md` — buyer-only playbook: real monetization math, 3-link placement, 30-day tracker, scaling past the first $10.
- `bonus/topic_engine.py` + `bonus/checklist.py` — the runnable tools.

## Principles

- **You stay in control.** The scheduler queues; a human approves every upload. No auto-post.
- **No copyright risk.** CC0/CC-BY visuals only, logged with source URLs.
- **No camera, no paid APIs** for the core path.

---

*Your channel, your rules. Human-approved publishing.*
