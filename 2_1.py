# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!


arr = [4,6,2,1,9,63,-134,566]  

def minimum(arr):
    min_arr = 0
    for i in arr: 
        if i < min_arr or len(arr) == 1: min_arr = i
    return min_arr 

def maximum(arr):
    max_arr = 0
    for i in arr:
        if i > max_arr: max_arr = i
    return max_arr   

print(f'min = {minimum(arr)}')  
print(f'max = {maximum(arr)}')  