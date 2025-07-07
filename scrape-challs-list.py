import requests
from bs4 import BeautifulSoup
from collections import defaultdict

# Replace with the base URL of the CTF event
BASE_URL = "https://example-ctf.com" # <--- REPLACE THIS
session = requests.Session()

# Example: Some CTFs require login — uncomment if needed
# login_url = f"{BASE_URL}/login"
# credentials = {'name': 'your_username', 'password': 'your_password'}
# session.post(login_url, data=credentials)

# Get the challenges page
challs_url = f"{BASE_URL}/challenges"
resp = session.get(challs_url)
soup = BeautifulSoup(resp.text, 'html.parser')

# CTFd platforms often load challenge data via JavaScript/API, so let's try the API endpoint
api_url = f"{BASE_URL}/api/v1/challenges"
resp = session.get(api_url)
data = resp.json()

# Organize challenges by category
categories = defaultdict(list)
for chall in data['data']:
    categories[chall['category']].append(chall['name'])

# Print as bullet points
for cat, challs in categories.items():
    print(f"- {cat}")
    for c in challs:
        print(f"  - {c}")

