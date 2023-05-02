# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

first = int(input())
second = int(input())

def sum(a, b, c = 0):
    c += 1
    if c == a + b:
        return c
    return sum(a, b, c)

print(sum(first, second))