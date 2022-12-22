#!/usr/bin/env python3

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N 

num = int(input('Enter a number number greater than 1: '))
fact = 1

if num > 1:
	for i in range(1, num+1):
		fact*=i
	print(fact)
else: 
	print('You entered incorrect number')