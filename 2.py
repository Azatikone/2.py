import requests
import os

download_folder = 'git_hellokuber_tenzor'
owner = "paulbouwer"
repo = "hello-kubernetes"
path = "src/app"
url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
files = requests.get(url).json()

for file in files:
    if file['type'] == 'file':
        download_url = file['download_url']
        content = requests.get(download_url).content
        filename = file['name']


