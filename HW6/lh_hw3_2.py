#!/usr/bin/env python3

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний

import random

size = int(input("Enter list's size: "))

# numbers = [] 
# for i in range(1, size + 1):
# 	numbers.append(random.randint(1,10))
# print(numbers)


# List comprehension 
numbers = [random.randint(1,10) for i in range (1, size + 1)]
print(numbers)

start = 0
end = size - 1
new_lst = [] 

while start <= end:
	new_lst.append(numbers[start] * numbers[end]) 
	start += 1
	end -= 1

print(new_lst)



