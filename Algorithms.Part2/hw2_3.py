#!/usr/bin/env python3

# Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.

num = int(input('Enter a number: '))

dictionary = {i: 1 + (1/i)**i for i in range(1, num+1)} 
print(dictionary)



