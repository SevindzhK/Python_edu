#!/usr/bin/env python3

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)

x = int(input('Enter x: '))
y = int(input('Enter y: ')) 

if x == 0 and y == 0:
	print('The point is at the origin')
elif x == 0:
	print('The point is on the y-axis')
elif y == 0: 
	print('The point is on the x-axis')
elif x > 0 and y > 0:
	print(1)
elif x < 0 and y > 0:
	print(2)
elif x < 0 and y < 0: 
	print(3)	
elif x > 0 and y < 0: 
	print(4)


	
