#!/usr/bin/env python3

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

numbers = [1.1, 1.2, 3.1, 5.1, 10.01]

# создаю новый массив без целой части
# new_numbers = []
# for i in range(len(numbers)):  
# 	new_numbers.append(numbers[i] % 1)


# List comprehension 
new_numbers = [numbers[i] % 1 for i in range(len(numbers))]
print(new_numbers)


max = new_numbers[0] 
min = new_numbers[1]
for i in range(len(new_numbers)): 
	if new_numbers[i] > max: 
		max = new_numbers[i] 
	elif new_numbers[i] < min: 
		min = new_numbers[i] 

print(numbers)
print('Разница между макс. и мин. значением дробной части: ')
print('{:.2}'.format(max - min)) 


