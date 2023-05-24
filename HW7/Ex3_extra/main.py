# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 

def print_operation_table(operation, num_rows=6, num_colums=6):
    for j in range(1, num_rows + 1):
        print(j, end='\t')
        if j == 1:
            for i in range(j + 1, num_colums + 1):
                print(i, end='\t')
        else:
            for i in range(2, num_colums + 1):
                print(operation(i, j), end='\t')
        print()
    

print_operation_table(lambda x, y: x + y)

