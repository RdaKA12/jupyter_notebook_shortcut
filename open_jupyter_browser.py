import os
import time
import re
import requests
import subprocess

# Get the Jupyter runtime directory
runtime_dir = os.path.expanduser(r'~\AppData\Roaming\jupyter\runtime')

print("[*] Waiting for Jupyter connection...")

# Wait up to 30 seconds for a Jupyter runtime file to appear
for i in range(30):
    # Find the most recent 'jpserver-*-open.html' file
    files = sorted(
        [f for f in os.listdir(runtime_dir) if f.startswith("jpserver") and f.endswith("-open.html")],
        key=lambda f: os.path.getmtime(os.path.join(runtime_dir, f)),
        reverse=True
    )
    if files:
        break
    time.sleep(1)

if not files:
    print("[!] No Jupyter connection file found.")
    exit(1)

# Read the tokenized HTML file
html_path = os.path.join(runtime_dir, files[0])

with open(html_path, 'r') as f:
    html = f.read()

# Extract the URL with the token
match = re.search(r'(http://localhost:\d+/tree\?token=[a-z0-9]+)', html)
if not match:
    print("[!] No Jupyter URL with token found.")
    exit(1)

url = match.group(1)

print(f"[*] Jupyter connection found: {url}")
print("[*] Waiting for the server to become ready...")

# Wait up to 30 seconds until the URL becomes reachable
for i in range(30):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            break
    except:
        pass
    time.sleep(1)

print("[*] Opening browser...")

# Replace with your browser's executable path (e.g., Chrome)
browser_path = r"<PATH_TO_YOUR_BROWSER_EXECUTABLE>"

subprocess.Popen([browser_path, url])
