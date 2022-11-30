#!/usr/bin/env python3

#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным. 

number = int(input('Enter day of week (number from 1 to 7): '))
if (number < 1 or number > 8):
	print('You entered incorrect number')
else:
	print(number == 6 or number == 7)
