# CTFd Challenge Scraper

This Python tool scrapes challenges, categories, descriptions, and downloadable files from a CTFd-based Capture The Flag platform. It organizes everything into a clean folder structure for offline solving and team collaboration.

## 🛠 Requirements
- Python 3.7+
- requests
- beautifulsoup4

Install dependencies:
```python
pip install requests beautifulsoup4
```

## 🧑‍💻 Usage
Run the script:
```bash
python3 generate.py --base-url https://example-ctf.com
```

### Optional Arguments:
| Flag                   | Description                                               |
| ---------------------- | --------------------------------------------------------- |
| `--scrape-description` | Include challenge descriptions in the writeups            |
| `--scrape-files`       | Download attached files for each challenge                |
| `--no-writeup`         | Skip generating the `writeup.md` template                 |
| `--list-only`          | Only print a bullet-point list of all challenges and exit |
| `--output-dir`         | Custom base folder for output (default: `./writeups`)     |

### Examples:
```bash
# Bullet point list
python3 generate.py --base-url https://example-ctf.com --list-only
# Full scraping + writeups
python3 generate.py --base-url https://example-ctf.com --scrape-description --scrape-files
# Files + description + no writeups
python3 generate.py --base-url https://your-ctf.com --scrape-description --scrape-files --no-writeup
```

## 📦 Output Structure
### Scrape files/descriptions
```bash
writeups/
├── [Category]/
│   └── [Challenge_Title]/
│       └── writeup.md
│       └── any_files.ext # (Optional) Challenge-provided files
```
### Challenge List
```bash
- [Category]
  - [Challenge_Title]
  - [Challenge_Title]
- [Category]
  - [Challenge_Title]
  - [Challenge_Title]
```

## Writeup template format
```
---
title: SSTI Basic
category: Web Exploitation
points: 100
date: 2025-07-07
tags: [ctf, web_exploitation]
---

# SSTI Basic | Web Exploitation | 100

Description: Exploit a basic SSTI vulnerability.

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
`CTF{example_flag_here}`
```

### 🔐 Notes on Login (If Required)
If the platform requires login:
1. Uncomment the login section in the script
2. Replace 'your_username' and 'your_password' with valid credentials

### 🧠 Tips
- You can rerun the script anytime — it won't overwrite files unless you delete the folders.
- Works with most CTFd instances (used by events like PicoCTF, TJCTF, etc.)
- For platforms not using CTFd (e.g., HackTheBox, custom platforms), this script will not work.

# 📜 License
This script is provided for personal and educational use. Use it responsibly and do not scrape private or restricted CTFs without permission.