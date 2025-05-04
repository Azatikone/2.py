
import requests
import os
import json
import zipfile
import datetime
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

logging.info('Создание папки')
download_fold='git_hellokuber_tenzor'
os.makedirs(download_fold, exist_ok=True)
url = "https://api.github.com/repos/paulbouwer/hello-kubernetes/contents/src/app"
files = requests.get(url).json()

logging.info('Запрос файлов из репозитория')
for file in files:
    if file['type'] == 'file':
        download_url = file['download_url']
        content = requests.get(download_url).content
        filename = file['name']
        n=open(f"{download_fold}/{filename}",'wb')
        n.write(content)

logging.info('Создание файла Version.json')
    pass

logging.info('Выгрузка версии')
with open("git_hellokuber_tenzor/package.json") as f:
    ver = json.load(f)['version']
with open('version.json', 'r') as f:
   data = json.load(f)
   data['version']= ver
with open('version.json', 'w') as f:
   json.dump(data, f)

logging.info('Создание списка фалов для файла Version.json')
names = [i for i in os.listdir('git_hellokuber_tenzor') if i.endswith('.js') or i.endswith('.py') or i.endswith('.sh')]

logging.info('Добавление списка names в файл Version.json')
with open('version.json', 'r+') as f:
   data = json.load(f)       #переделать (удалить эту строчку т.к. то же есть в 38 строке?
   data['files']= names
   f.seek(0)
   json.dump(data, f)

logging.info('Упаковка файлов в архив')
date = datetime.date.today().strftime('%d%m%Y')
folder = 'git_hellokuber_tenzor'
files_to_add = os.listdir(folder)
with zipfile.ZipFile(f'Архив app{date}.zip', "a") as mz:
    for file in files_to_add:
        mz.write(os.path.join(folder, file))


