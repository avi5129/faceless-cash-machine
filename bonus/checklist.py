#!/usr/bin/env python3
"""
checklist.py — Faceless Shorts daily production checklist generator.

Standard library only. Produces a printable checklist for a batch of N videos
so the human-in-the-loop never misses a quality gate.

Usage:
    python checklist.py --date 2026-07-19 --count 3
"""
import argparse
import datetime


GATES = [
    "Script: hook in first 1.5s, payload tight, CTA present",
    "Voice: normalized to -14 LUFS, true-peak <= -1 dBTP",
    "Visuals: only CC0 / CC-BY clips, source URL logged",
    "Captions: stable-ts word-level, gold #F5C518, safe area",
    "Edit: 2.5-4s shots, gold-wipe transition, 1080x1920 30fps",
    "Hook rotation: not repeating yesterday's hook variant",
    "Thumbnail/text: bold, readable on phone in <1s",
    "Human approval before publish (NO auto-post)",
]


def main():
    ap = argparse.ArgumentParser(description="Daily faceless Shorts checklist")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--count", type=int, default=3)
    args = ap.parse_args()

    print(f"=== Faceless Shorts — Production Checklist ===")
    print(f"Date: {args.date}   Target videos: {args.count}")
    print("=" * 46)
    for v in range(1, args.count + 1):
        print(f"\n--- Video {v} ---")
        for i, g in enumerate(GATES, 1):
            print(f"  [ ] {g}")
    print("\nReminder: publish 3/day max. Human approves every upload.")


if __name__ == "__main__":
    main()
