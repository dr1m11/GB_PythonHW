# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника). Числа вводятся построчно.

n = int(input())
m = int(input())
k = int(input())

def otlom(n, m, k):
    if k == n * m:
        return 'Долька равна размеру шоколада'
    mal = min(n, m)
    bol = max(n, m)
    for i in range(1, mal + 1):
        if (i * mal) == k:
            return 'Да'
    for i in range(1, bol):
        if (i * bol) == k:
            return 'Да'
    return 'Нет'

print(otlom(n, m, k))
            