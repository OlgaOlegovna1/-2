# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

n = int(input("Введите число: "))
dict_1 = []
for i in range(n):
    dict_1.append(randint(-10, 20))

    print(dict_1)
x = int(input("Введите позицию 1: "))

z = int(input("Введите позицию 2: "))
p = dict_1[x]*dict_1[z]
print(p)