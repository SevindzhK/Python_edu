#!/usr/bin/env python3

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

number = int(input('Enter natural number: ')) 
multipliers = []

if number > 0: 
	i = 2
	while i < number: 
		if i % 2 == 0 and i != 2: 
			i += 1
		while number % i == 0: 
			multipliers.append(i)
			number /= i 
		i += 1
	print (multipliers) 
	
else: 
	print('You entered incorrect number')




