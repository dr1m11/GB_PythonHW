def count_glas(x):
    x = x.lower()
    alfabet = 'ёуеыаоэяию'
    count = 0
    for i in x:
        for j in alfabet:
            if j == i:
                count += 1
                break
    return count
phrase = list(map(count_glas, input().split()))
checker = phrase[0]
flag = True
for i in phrase:
    if i != checker:
        flag = False
if flag: print("Парам пам-пам")
else: print('Пам парам')

