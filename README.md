# CTFd Challenge Scraper

This Python tool scrapes challenges, categories, descriptions, and downloadable files from a CTFd-based Capture The Flag platform. It organizes everything into a clean folder structure for offline solving and team collaboration.

## 🚀 Features
- Auto-discovers all challenges and categories
- Saves each challenge's description in a README.md
- Downloads any attached challenge files
- Organizes everything by category in folders

## 📦 Output Structure
```bash
./[Category]/
    └── [Challenge_Title]/
        ├── README.md        # Contains description
        └── any_files.ext    # Challenge-provided files (ZIP, PCAP, BIN, etc.)
```
### Example:
```
./Web_Exploitation/SSTI_Basic/
├── README.md
└── exploit.zip
```

## 🧑‍💻 Usage
1. Edit the script and set your CTF platform URL:
```bash
BASE_URL = "https://your-ctf-url.com"
```
2. Run the script in your desired folder:
```bash
# Scrape files and descriptions
python scrape-everything.py
# Scrape challenge names + categories
python scrape-challs-list.py
```
3. All challenges will be saved to folders by category.

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