#!/usr/bin/env python3

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input('Enter the number: ')) 
ostatok = 0
result = ''
while number > 0:
	ostatok = str(number % 2) 
	result += ostatok 
	number //= 2

result = ''.join(reversed(list(result)))
print(int(result)) 

