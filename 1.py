import requests
import time
start_time = time.time()
response = requests.get('https://yandex.com/time/sync.json?geo=213')
contents = response.text
print(contents)

r=requests.get('https://yandex.com/time/<title>14:59 — Москва — Яндекс.Время</title>').headers['Date'].split()[4].split(':')[:2]
print('Москва ',int(r[0])+3,':',*r[1:], sep='')

end_time = time.time()
print(end_time-start_time)

t=0
for i in range(5):
    t+=(end_time-start_time)
print('Дельта:',t/5)