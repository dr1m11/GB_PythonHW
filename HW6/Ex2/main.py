#  Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

first = int(input())
second = int(input())
arr = [1, 3, 7, 10, 5, 8]

for i in arr:
    if first <= i <= second:
        print(arr.index(i))