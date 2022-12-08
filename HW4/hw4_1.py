#!/usr/bin/env python3
import math 
import re 

#Вычислить число Пи c заданной точностью d 


number_d = str(input('Задайте точность d для числа Пи, где 10^-1 ≤ d ≤10^-10. \nНапример, 0.0001:  \n')) 

if not re.match(r'([0]\.[0]{,9}[1]{1}$)', number_d): 
	print('Incorrect input') 
	exit() 

print('Число Пи с точностью d: ')
print(str(math.pi)[0:len(number_d)])
