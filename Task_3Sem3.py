# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

first_list=[1.002, 4.1, 2, 4, 9.0012]
arrey=[]
for i in range(len(first_list)):
    arrey.append(first_list[i] - round(first_list[i]))
result = max(arrey) - min(arrey)
print(result)

