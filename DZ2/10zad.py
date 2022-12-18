# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2
from random import randint
n = int(input('Введите число '))
l = [randint(0,1 ) for i in range(0, n)]
count = 0
count1=0
max=0
for el in l:
    if el == 0:
        count+=1
for el in l:
    if el == 1:
        count1+=1
if count>=count1:
    print(count1)
else:
    if count1>=count:
        print(count)


print(l)
print(count)
print(count1)
