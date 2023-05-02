#  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

first = int(input())
second = int(input())

def step(a, b):
    c = a ** b
    p = a
    def step2(a):
        if a == c:
            return a
        return step2(a * p)
    return step2(a)
    


print(step(first, second))
