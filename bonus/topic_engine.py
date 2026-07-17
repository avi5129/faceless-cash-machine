#!/usr/bin/env python3
"""
topic_engine.py — Faceless Shorts topic + hook generator.

Standard library only. No pip install required.

Each topic maps to a curated keyword so hook lines read naturally
(e.g. "compounding", "black holes") instead of awkward word-slices.

Usage:
    python topic_engine.py --niche finance --count 10
    python topic_engine.py --niche science --count 5 --seed 7 --json
"""
import argparse
import json
import random
import sys

# (topic, keyword) — keyword is the clean noun used inside hook lines.
NICHE_TOPICS = {
    "finance": [
        ("The 50/30/20 rule that quietly builds wealth", "the 50/30/20 rule"),
        ("Why compounding beats timing the market", "compounding"),
        ("The expense most people forget to cut", "hidden expenses"),
        ("How a single index fund outperforms most traders", "index funds"),
        ("The emergency fund number nobody tells you", "emergency funds"),
        ("What rich people do with their paycheck first", "paycheck habits"),
        ("The tax move that saves freelancers thousands", "freelancer taxes"),
        ("Why your savings account is losing money", "savings accounts"),
        ("The debt order that frees you fastest", "debt payoff"),
        ("How to automate your investing in 10 minutes", "automated investing"),
    ],
    "science": [
        ("What actually happens inside a black hole", "black holes"),
        ("Why your gut has a second brain", "your gut brain"),
        ("The element that falls through your hand", "liquid metal"),
        ("How octopuses rewrite their own RNA", "octopus RNA"),
        ("Why we yawn when we see others yawn", "contagious yawning"),
        ("The speed limit nothing can break", "the speed of light"),
        ("How trees talk to each other underground", "tree networks"),
        ("Why glass is technically a liquid", "glass flow"),
        ("What zero gravity does to your body", "zero gravity"),
        ("The coldest place in the universe", "absolute zero"),
    ],
    "history": [
        ("The map that almost ended the world", "a forbidden map"),
        ("The letter that changed an empire", "a lost letter"),
        ("Why a volcano erased a summer", "the volcano year"),
        ("The bet that bought an island", "a strange bet"),
        ("The code that took a century to break", "an unbroken code"),
        ("The accident that invented a continent's food", "a kitchen accident"),
        ("Why clocks were once a crime", "clock crimes"),
        ("The voyage nobody believed happened", "a hidden voyage"),
        ("The weapon too strange to use", "a strange weapon"),
        ("How a typo redrew a border", "a map typo"),
    ],
    "productivity": [
        ("The 2-minute rule that beats procrastination", "the 2-minute rule"),
        ("Why your to-do list is making you tired", "your to-do list"),
        ("The focus method used by surgeons", "deep focus"),
        ("How to finish books you start", "book finishing"),
        ("The sleep habit that boosts memory", "sleep habits"),
        ("Why deep work beats long hours", "deep work"),
        ("The meeting rule that saves your week", "meeting rules"),
        ("How to learn anything in 20 hours", "rapid learning"),
        ("The inbox system that ends email stress", "inbox zero"),
        ("Why writing things down makes you smarter", "note-taking"),
    ],
    "animals": [
        ("The frog that freezes solid and revives", "the frozen frog"),
        ("Why octopuses escape any tank", "octopus escapes"),
        ("The bird that remembers faces", "face-remembering birds"),
        ("How ants build living bridges", "ant bridges"),
        ("The shrimp louder than a jet engine", "the loud shrimp"),
        ("Why cats knead before they sleep", "cat kneading"),
        ("The fish that climbs trees", "tree-climbing fish"),
        ("How elephants speak underground", "elephant rumble"),
        ("The lizard that walks on water", "water-walking lizards"),
        ("Why dogs tilt their heads at you", "dog head tilts"),
    ],
}

HOOKS = [
    "Stop scrolling — this changes how you think about {n}.",
    "Nobody talks about this, but {n} is the real secret.",
    "I wish someone told me about {n} sooner.",
    "The truth about {n} they don't teach in school.",
    "This one fact about {n} will surprise you.",
    "You've been wrong about {n} this whole time.",
]

CTAS = [
    "Follow for part 2.",
    "Save this before you forget it.",
    "Comment your biggest takeaway.",
    "Subscribe — more like this daily.",
]


def generate(niche, count, seed=None):
    topics = NICHE_TOPICS.get(niche.lower())
    if not topics:
        avail = ", ".join(NICHE_TOPICS.keys())
        print(f"Unknown niche '{niche}'. Available: {avail}", file=sys.stderr)
        sys.exit(1)
    rng = random.Random(seed)
    out = []
    for i in range(count):
        topic, keyword = rng.choice(topics)
        hook = rng.choice(HOOKS).format(n=keyword)
        cta = rng.choice(CTAS)
        out.append({
            "id": i + 1,
            "topic": topic,
            "keyword": keyword,
            "hook": hook,
            "cta": cta,
        })
    return out


def main():
    ap = argparse.ArgumentParser(description="Faceless Shorts topic + hook generator")
    ap.add_argument("--niche", default="finance", help="finance|science|history|productivity|animals")
    ap.add_argument("--count", type=int, default=10)
    ap.add_argument("--seed", type=int, default=None, help="deterministic output")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    args = ap.parse_args()

    results = generate(args.niche, args.count, args.seed)
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            print(f"[{r['id']:02d}] {r['hook']}")
            print(f"     Topic: {r['topic']}")
            print(f"     CTA:   {r['cta']}")
            print()


if __name__ == "__main__":
    main()
