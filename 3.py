import random
import json


conf = {"Sh1": "3.7.*", "Sh2": "3.*.1", "Sh3": "1.2.3.*"}
with open('confile.json', 'w') as f:
    json.dump(conf, f)

num = '3.7.9'  #input() сделать в конце

result = {}
for key, value in conf.items():
    vers = []
    for _ in range(10):
        parts = value.split('.')
        new_parts = []
        for p in parts:
            if p == '*':
                new_parts.append(str(random.randint(0, 9)))
            else:
                new_parts.append(p)
        vers.append('.'.join(new_parts))
    vers1 = list(set(vers))
    result[key] = vers1
print(result)

finlist1=[]
finlist2=[]
finlist3=[]
Sh1=''
Sh2=''
Sh3=''
r=0

dl = len(num)
for i in result.items():
    for j in i[1]:
        ind = list(conf.values())[int(i[0][-1]) - 1].find('*')
        if ''.join(j[0:ind].split('.')) <= ''.join(num[0:ind].split('.')):
            if dl==len(i[1][0]):
                if i[0]=='Sh1':
                    if int(num[ind]) > int(j[ind]):
                        finlist1.append(j)
                        Sh1 = 'Sh1'
                if i[0]=='Sh2':
                    if int(num[ind]) > int(j[ind]):
                        finlist2.append(j)
                        Sh2 = 'Sh2'
                if i[0]=='Sh3':
                    if int(num[ind]) > int(j[ind]):
                        finlist3.append(j)
                        Sh3 = 'Sh3'
ud = 'удовлетворяет'
print(Sh1, *finlist1)
print(Sh2, *finlist2)
print(Sh3, *finlist3)