# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input('Введите преобразуемое число: '))
rem = ''
while num > 0:
    rem = str(num % 2) + rem
    num = num // 2
 
print(rem)