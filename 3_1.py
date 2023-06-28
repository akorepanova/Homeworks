# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

import random
from tabulate import tabulate
from pprint import pprint

class Matrix:
    
    def __init__(self):
        self.matrix = self.create_matrix()
        
    def create_matrix(self):
        matrix = []
        rows = random.randint(1,10)
        colums = random.randint(1,10)
        for i in range(rows):
            y = ([(random.randint(1,99)) for j in range(colums)])
            matrix.append(y)
        print("Матрица создана:\n", tabulate(matrix))
        # pprint(matrix)
        return matrix
        
    def edit_cell_of_matrix(self):
        try:
            cell = ([int(i) for i in 
                    input("Выбери строку и столбец для изменения значения в ячейке: ")
                    .split(" ")])
            print(f'Ячейка для изменений (строка, столбец): {cell}\n'
              f'Текущее значение ячейки: {self.matrix[cell[0]-1][cell[1]-1]}')
        except IndexError:
            print("Указанной ячейки не существует!")
            return
        except ValueError: 
            print("Указанной ячейки не существует!")
            return
        
        
        try:
            new_data_cell = int(input("Новое значение для данной ячейки: "))
            print(f'Внесены новые данные: {new_data_cell}')
        except ValueError:
            print("Внесены некорректные данные!")
            new_data_cell = 'None'
        self.matrix[cell[0]-1][cell[1]-1] = new_data_cell
        # pprint(self.matrix)
        print(tabulate(self.matrix))

    def get_matrix_size(self):
        print(f'Число строк в данной матрице: {len(self.matrix)}\n' +
              f'Число столбцов в данной матрице: {len(self.matrix[0])}')

matrix2 = Matrix()
matrix2.edit_cell_of_matrix()
matrix2.get_matrix_size()