#!/usr/bin/env python3

#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции

numbers = [3, -5, 4, 25, -7, 9, 11, 21, 1]

def sum(lst):
	summa = 0
	for i in range(1, len(lst)-1, 2):
		summa += lst[i]
	return summa
print(sum(numbers)) 


