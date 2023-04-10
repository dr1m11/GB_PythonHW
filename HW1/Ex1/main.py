# Найдите сумму цифр трехзначного числа.

def numSum3Digit(num):
    strNum = str(num)
    return int(strNum[0]) + int(strNum[1]) + int(strNum[2])

res = numSum3Digit(123)
print(res)