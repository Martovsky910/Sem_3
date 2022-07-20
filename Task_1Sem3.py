from typing import List


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list = [1, 2, 3, 4, 5, 6]

def Sum_elements(list):
    sum = 0 
    for e in list:
        if e % 2==0:
            sum += e
    return sum

print(Sum_elements(list))