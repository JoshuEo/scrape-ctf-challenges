import requests
import argparse
from collections import defaultdict
from pathlib import Path
from datetime import datetime
from urllib.parse import urljoin
from html import unescape

# ---------------------
# CLI Argument Parsing
# ---------------------
parser = argparse.ArgumentParser(description="CTFd Writeup Generator & Challenge Lister")
parser.add_argument("--scrape-description", action="store_true", help="Include challenge descriptions")
parser.add_argument("--scrape-files", action="store_true", help="Download challenge files")
parser.add_argument("--no-writeup", action="store_true", help="Do not generate writeup.md templates")
parser.add_argument("--list-only", action="store_true", help="Only print a bullet list of challenges and exit")
parser.add_argument("--output-dir", type=str, default="./writeups", help="Base output directory")
parser.add_argument("--base-url", type=str, required=True, help="Base URL of the CTF platform (no trailing slash)")
args = parser.parse_args()

BASE_URL = args.base_url.rstrip("/")
OUTPUT_DIR = Path(args.output_dir)
session = requests.Session()

# Optional login
# login_url = f"{BASE_URL}/login"
# credentials = {'name': 'your_username', 'password': 'your_password'}
# session.post(login_url, data=credentials)

# Fetch challenges list
api_url = f"{BASE_URL}/api/v1/challenges"
resp = session.get(api_url)
data = resp.json()

# List-only mode: just print bullet list and exit
if args.list_only:
    categories = defaultdict(list)
    for chall in data["data"]:
        categories[chall["category"]].append(chall["name"])

    print("\n🎯 Challenge List:\n")
    for category, challenges in categories.items():
        print(f"- {category}")
        for chall in challenges:
            print(f"  - {chall}")
    print("\n✅ Done (list-only mode).")
    exit(0)

# Process each challenge
for chall in data["data"]:
    chall_id = chall["id"]
    title = chall["name"]
    category = chall["category"]
    points = chall.get("value", 0)
    tags = ["ctf", category.lower().replace(" ", "_")]
    date = datetime.now().strftime("%Y-%m-%d")

    safe_category = category.replace(" ", "_")
    safe_title = title.replace(" ", "_").replace("/", "_")
    writeup_dir = OUTPUT_DIR / safe_category / safe_title
    writeup_dir.mkdir(parents=True, exist_ok=True)

    description = "No description available."
    files_downloaded = []

    if args.scrape_description or args.scrape_files:
        detail_api = f"{BASE_URL}/api/v1/challenges/{chall_id}"
        detail_resp = session.get(detail_api)
        detail_data = detail_resp.json().get("data", {})

        if args.scrape_description:
            description = unescape(detail_data.get("description", "No description"))

        if args.scrape_files:
            for file_url in detail_data.get("files", []):
                full_url = urljoin(BASE_URL, file_url)
                filename = file_url.split("/")[-1]
                file_resp = session.get(full_url)
                file_path = writeup_dir / filename
                with open(file_path, "wb") as f:
                    f.write(file_resp.content)
                files_downloaded.append(filename)
                print(f"📦 Downloaded: {file_path}")

    if not args.no_writeup:
        template = f"""---
title: {title}
category: {category}
points: {points}
date: {date}
tags: [{', '.join(tags)}]
---

# {title} | {category} | {points}

Description: {description}

---

## Table of Contents
- [Overview](#overview)
- [Enumeration](#enumeration)
- [Exploitation](#exploitation)
- [Flag](#flag)

---

## Overview
*Summarize what kind of challenge this is and any hints or clues.*

## Enumeration
*Write down the steps you took to analyze the file or service.*

## Exploitation
*Detail the exact steps or code used to exploit the challenge.*

## Flag
`CTF{{example_flag_here}}`
"""
        writeup_path = writeup_dir / "writeup.md"
        with open(writeup_path, "w", encoding="utf-8") as f:
            f.write(template)
        print(f"✅ Created writeup: {writeup_path}")

print(f"\n🎯 Done. All output saved in: {OUTPUT_DIR.resolve()}")