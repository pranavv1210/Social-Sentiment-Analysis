#!/usr/bin/env python3
"""Convert TweetClaw exports into the dashboard's tweet CSV shape."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any, Iterable

FIELDNAMES = [
    "airline_sentiment",
    "airline",
    "text",
    "tweet_created",
    "clean_text",
    "source_id",
    "author_username",
]

TEXT_KEYS = ("text", "full_text", "tweet_text", "content", "body", "tweet")
CREATED_KEYS = ("tweet_created", "created_at", "createdAt", "created")
ID_KEYS = ("id", "tweet_id", "tweetId", "rest_id", "restId")
AUTHOR_KEYS = ("author_username", "username", "screen_name", "screenName")
COLLECTION_KEYS = ("data", "tweets", "results", "items", "records", "posts")


def clean_text(value: str) -> str:
    value = re.sub(r"http\S+|www\S+|https\S+", " ", value)
    value = re.sub(r"@\w+|#", " ", value)
    value = re.sub(r"[^A-Za-z0-9\s]", " ", value)
    return " ".join(value.lower().split())


def first_text(row: dict[str, Any], keys: Iterable[str]) -> str:
    for key in keys:
        value = row.get(key)
        if value is not None and str(value).strip():
            return str(value).strip()
    return ""


def normalize_record(row: dict[str, Any]) -> dict[str, str] | None:
    text = first_text(row, TEXT_KEYS)
    if not text:
        return None
    sentiment = first_text(row, ("airline_sentiment", "sentiment", "label")) or "unlabeled"
    airline = first_text(row, ("airline", "brand", "topic")) or "TweetClaw"
    return {
        "airline_sentiment": sentiment,
        "airline": airline,
        "text": text,
        "tweet_created": first_text(row, CREATED_KEYS),
        "clean_text": clean_text(text),
        "source_id": first_text(row, ID_KEYS),
        "author_username": first_text(row, AUTHOR_KEYS),
    }


def records_from_json(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, list):
        return [item for item in value if isinstance(item, dict)]
    if isinstance(value, dict):
        for key in COLLECTION_KEYS:
            nested = value.get(key)
            if isinstance(nested, list):
                return [item for item in nested if isinstance(item, dict)]
        return [value]
    return []


def read_records(path: Path) -> list[dict[str, Any]]:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        with path.open(newline="", encoding="utf-8") as handle:
            return list(csv.DictReader(handle))

    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    if suffix != ".jsonl" and text[0] in "[{":
        try:
            return records_from_json(json.loads(text))
        except json.JSONDecodeError:
            pass

    rows: list[dict[str, Any]] = []
    for line in text.splitlines():
        if line.strip():
            value = json.loads(line)
            if isinstance(value, dict):
                rows.append(value)
    return rows


def convert(input_path: Path, output_path: Path) -> int:
    rows = [row for item in read_records(input_path) if (row := normalize_record(item))]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare TweetClaw tweet exports for this dashboard.")
    parser.add_argument("input", type=Path, help="TweetClaw JSON, JSONL, or CSV export")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/tweetclaw_tweets.csv"),
        help="Output CSV path",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    count = convert(args.input, args.output)
    print(f"Wrote {count} rows to {args.output}")


if __name__ == "__main__":
    main()
