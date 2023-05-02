# Заполните массив элементами арифметической прогрессии. Её первый элемент(a1), разность(d) и количество элементов(n) нужно ввести с клавиатуры.

a1 = int(input())
d = int(input())
n = int(input())

def fill_array(a1, d, n, arr = [a1]):
    curr = a1
    for i in range(n - 1):
        curr += d
        arr.append(curr)
    return arr
print(*fill_array(a1, d, n))