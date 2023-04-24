print('Введите количество элементов первого набора чисел')
first = [int(x) for x in range(int(input()))]
print('Введите количество элементов второго набора чисел')
second = [int(x) for x in range(int(input()))]

print('Введите элементы первого набора чисел')
for i in range(len(first)):
    num = int(input())
    first[i] = num

print("Введите элементы второго набора чисел")
for i in range(len(second)):
    num = int(input())
    second[i] = num

arr = []

for i in first:
    if (i in second) and (not(i in arr)):
        arr.append(i)
print(sorted(arr))
