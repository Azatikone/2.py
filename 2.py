import requests
import os

download_fold='git_hellokuber_tenzor'
os.makedirs(download_fold, exist_ok=True)

url = "https://api.github.com/repos/paulbouwer/hello-kubernetes/contents/src/app"
files = requests.get(url).json()

for file in files:
    if file['type'] == 'file':
        download_url = file['download_url']
        content = requests.get(download_url).content
        filename = file['name']
        n=open(f"{download_fold}/{filename}",'wb')
        n.write(content)
