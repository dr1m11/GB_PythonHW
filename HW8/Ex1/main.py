def search():
    with open('numbers.txt', 'r') as data:
        a = data.read()
    data = a.split('\n')
    name = input('Введите имя ')
    return list(filter(lambda a: name in a, data))


def change_data() -> None:
    while True:
        name = search()
        if len(name) == 1:
            name = ''.join(name)
            with open('numbers.txt', 'r') as data:
                a = data.read()
            data = a.split('\n')
            arr = []
            for i in data:
                if not(name in i) or not(i in name):
                    arr.append(i + '\n')
                else:
                    arr.append(input('Введите ФИО | Номер телефона ') + '\n')
            with open('numbers.txt', 'w') as book:
                book.write('')
            with open('numbers.txt', 'a') as book:
                book.writelines(arr)
            break
        print('Введите полное ФИО')

def delete_data() -> None:
    while True:
        name = search()
        if len(name) == 1:
            name = ''.join(name)
            with open('numbers.txt', 'r') as data:
                a = data.read()
            data = a.split('\n')
            arr = []
            for i in data:
                if not(name in i) or not(i in name):
                    arr.append(i + '\n')
            with open('numbers.txt', 'w') as book:
                book.write('')
            with open('numbers.txt', 'a') as book:
                book.writelines(arr)
            break
        print('Введите полное ФИО')

print(delete_data())
    
    