# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

first_list = list(map(int,input('Введите числа через пробел: ').split()))
print(first_list)

def mult(numbers):
    second_list = []
    while len(numbers) > 1:
        second_list.append(numbers[0]*numbers[-1])
        del numbers[0] 
        del numbers[-1] 
    if len(numbers) ==1: 
        second_list.append(numbers[0]**2)       
    return second_list

print(mult(first_list))