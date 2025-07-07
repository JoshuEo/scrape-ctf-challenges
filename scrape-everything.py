import os
import requests
from pathlib import Path
from html import unescape
from urllib.parse import urljoin

# Set your CTF platform URL here (no trailing slash)
BASE_URL = "https://example-ctf.com"  # <- CHANGE THIS
session = requests.Session()

# Optional: Login (if required)
# login_url = f"{BASE_URL}/login"
# credentials = {'name': 'your_username', 'password': 'your_password'}
# session.post(login_url, data=credentials)

# Get challenge metadata
challenges_api = f"{BASE_URL}/api/v1/challenges"
resp = session.get(challenges_api)
challenges = resp.json().get("data", [])

# Loop through each challenge
for chall in challenges:
    chall_id = chall['id']
    title = chall['name']
    category = chall['category']

    # Get detailed info (description, files)
    chall_detail_url = f"{BASE_URL}/api/v1/challenges/{chall_id}"
    detail_resp = session.get(chall_detail_url)
    detail = detail_resp.json().get("data", {})

    # Create folder structure: ./[Category]/[Challenge_Title]/
    safe_category = category.replace(" ", "_")
    safe_title = title.replace(" ", "_").replace("/", "_")
    folder_path = Path(f"./{safe_category}/{safe_title}")
    folder_path.mkdir(parents=True, exist_ok=True)

    # Write README.md with description
    description = unescape(detail.get("description", "No description"))
    readme_path = folder_path / "README.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n**Category**: {category}\n\n## Description\n\n{description}\n")

    # Download any files
    for file_url in detail.get("files", []):
        full_url = urljoin(BASE_URL, file_url)
        filename = file_url.split("/")[-1]
        file_resp = session.get(full_url)
        file_path = folder_path / filename
        with open(file_path, "wb") as f:
            f.write(file_resp.content)
        print(f"Downloaded: {file_path}")

print("✅ Done. All challenges saved with descriptions and files.")
