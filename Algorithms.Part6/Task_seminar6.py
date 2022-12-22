#!/usr/bin/env python3


# 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:* 2+2 => 4;  1+2*3 => 7;   1-2*3 => -5;

ex = '2 * 3 - 7' 
ex = ex.split() 
print(ex) 

for i in range(len(ex)): 
	if ex[i] == '*':
		result = int(ex[i-1]) * int(ex[i+1])
		if ex[i-2] == '-': 
			result *= -1 
			ex[i-2] = 0
		ex[i-1] = 0
		ex[i] = 0
		ex[i+1] = 0
	elif ex[i] == '/': 
		result = int(ex[i-1]) / int(ex[i+1])
		if ex[i-2] == '-': 
			result *= -1 
			ex[i-2] = 0
		ex[i-1] = 0
		ex[i] = 0
		ex[i+1] = 0 


for i in range(len(ex)): 
	if ex[i] == '-': 
		ex[i+1] = int(ex[i+1]) * -1
		ex[i] = 0
	result += int(ex[i])

print(result) 