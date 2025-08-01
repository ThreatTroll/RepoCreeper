import requests
import urllib.parse
import time
from getpass import getpass
from rich.console import Console
from rich.text import Text
from pyfiglet import Figlet

console = Console()
fig = Figlet(font="slant")  # You can try 'standard', 'slant', 'block', etc.

# Create big text
banner_text = fig.renderText("RepoCreeper")

# Style banner: cyan + bold
styled_banner = Text(banner_text, style="bold cyan")

# Style tagline
tagline = Text("we see your commits-ThreatTroll", style="italic green")

# Print to terminal
console.print(styled_banner)
console.print(tagline)

GITHUB_TOKEN = input("Please Enter your github token: ")

input_keywords = input("Enter keywords (comma-separated): ")
keywords = [k.strip() for k in input_keywords.split(",") if k.strip()]

dorks = [
    'in:file',
    'extension:py',
    'extension:js',
    'extension:yaml',
    'extension:env',
    'extension:json',
    'extension:cs',
    'filename:.gitignore',
    'filename:TheGroup.pfx',
    'path:/config'
]

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {GITHUB_TOKEN}"
}


def search_github(query):
    base_url = "https://api.github.com/search/code"
    params = {"q": query, "per_page": 5}
    results = []

    while True:
        response = requests.get(base_url, headers=headers, params=params)

        if response.status_code == 200:
            items = response.json().get("items", [])
            for item in items:
                results.append({
                    "file_url": item["html_url"],
                    "repo_name": item["repository"]["full_name"]
                })
            return results

        elif response.status_code == 401:
            print("❌ 401 Unauthorized: Invalid token.")
            break

        elif response.status_code == 403:
            print("⏳ Rate limited. Waiting 60 seconds...")
            time.sleep(60)
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
            break

    return []


all_matches = {}

for keyword in keywords:
    all_matches[keyword] = []
    print(f"\n🔍 Searching: {keyword}")
    for dork in dorks:
        query = f'" {keyword} " {dork}'
        print(f" → Dork: {query}")
        urls = search_github(query)
        all_matches[keyword].extend(urls)
        time.sleep(2)

print("\n✅ Results:")
for keyword, matches in all_matches.items():
    print(f"\n🔑 Keyword: {keyword} ({len(matches)} results):")
    for match in matches:
        print(f" - Repo: {match['repo_name']}\n   URL:  {match['file_url']}")
