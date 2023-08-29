# CodeWhisper: Extract Silent Whispers from Web Content

**CodeWhisper** delves into the depths of web content to extract the silent "whispers" or notes developers often leave behind. Using the raw power of `feroxbuster`, this tool scours HTML and JS files for developer comments that may provide invaluable insights.

---
## Requirements:
- poetry for Python dependency management
- feroxbuster for content discovery
---

## Quick Start:

```bash
# 1. Clone the repository
git clone <repository-url>

# 2. Navigate to the CodeWhisper directory
cd CodeWhisper

# 3. Set up the environment
## Install poetry
pip install poetry

## Use poetry for dependency management
poetry install

# 4. Activate the virtual environment
poetry shell

# 5. Run feroxbuster to discover the Web Content & output a .json
feroxbuster -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories-lowercase.txt -u http://$IP -t 50 --no-recursion -o input.file --json

# 6. Extract developer comments using CodeWhisper
python main.py

```
---

## About:
### Why CodeWhisper?

During pentesting or web development analysis, uncovering developer comments can be the key to discovering potential vulnerabilities, hidden functionalities, or understanding the inner workings of a web application. CodeWhisper makes this process streamlined and efficient.

### How does it work?

CodeWhisper uses feroxbuster to perform content discovery against the specified target. It then processes the JSON output, searching for comments in HTML and JS files that might have been left behind by developers.

---
## Contributions:
Feel free to fork, improve, make pull requests or fill issues. Every contribution is welcome!

---
## Disclaimer:
This tool is intended for educational purposes and ethical use only. Ensure you have proper authorization before probing any web application.

