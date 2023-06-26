# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
greeting = my_favorite_songs

#Первый трек
print (greeting[:14])

#Последний трек
print (greeting[-13:])

#Второй трек
print (greeting[16:30])

#Второй трек с конца
print (greeting[-26:-15])