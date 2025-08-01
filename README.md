
# 🕵️‍♂️ RepoCreeper

**RepoCreeper** is an automated GitHub source code and secret discovery tool. It searches for keywords (e.g., internal project names, environment files, leaked keys) across GitHub repositories using intelligent dorks and GitHub’s Code Search API.

> 🔐 Ideal for CTI analysts, red teamers, and OSINT researchers tracking leaks, misconfigs, and exposed dev artifacts.

<img width="824" height="274" alt="image" src="https://github.com/user-attachments/assets/71c22ee3-5720-4e6b-bbc0-0059fcf8db10" />


---

## 🚀 Features

- 🔍 Keyword-based GitHub code search
- 🧠 Smart dork combinations (`in:file`, `extension:env`, etc.)
- 🔗 Outputs full file URLs and repository names
- 🔐 GitHub token authentication (avoids rate limits)
- 🧑‍💻 Interactive CLI input for ease of use

---

## 🧠 Dorks Used
For each keyword, the following GitHub code search filters are applied:

- in:file
- extension:py
- extension:js
- extension:yaml
- extension:env
- extension:json
- extension:cs
- filename:.gitignore
filename:TheGroup.pfx
path:/config

---

## 📦 Requirements

- Python 3.7+
- `requests` library


🔐 Getting a GitHub Token
To avoid GitHub rate limits:

Go to https://github.com/settings/tokens

Generate a Classic Token with no scopes

Copy the token (starts with ghp_...)

Paste it when prompted

⚡ Quick Start
# 1. Clone or download the tool
- git clone [https://github.com/ThreatTroll/RepoCreeper.git]
- cd repocreeper
- python -m venv venv
- source venv/bin/activate      # On Windows: venv\\Scripts\\activate
- pip install -r requirements.txt


# 3. Run the tool
python repocreeper.py

