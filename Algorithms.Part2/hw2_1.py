#!/usr/bin/env python3

#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.(Сделать для строки)

str_num = input('Enter real number with "."')
num = int(str_num.replace('.',''))
summa = 0

while num > 0:
	ostatok = num % 10
	summa += ostatok
	num //= 10
print(summa)

