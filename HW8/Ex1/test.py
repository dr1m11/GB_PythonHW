name = 'Исаев Владислав Иванович | +814881481848'

with open('numbers.txt', 'r') as data:
    a = data.read()
data = a.split('\n')
for i in data:
    if i == name:
        print('zbs')
    else: print('huevo')

