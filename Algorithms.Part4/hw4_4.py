#!/usr/bin/env python3
import random 

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)* многочлена и записать в файл многочлен степени k.
#     *Пример:*  k=2   =>   2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 


k = int(input('Задайте натуральную степень k: ')) 
string = f'{random.randint(0,100)} * x^{k}'


while k >= 2:
		if k == 2: 
			string = string + f'+{random.randint(0,100)} * x+{random.randint(0,100)}'
		else: 
			string = string + f'+{random.randint(0,100)} * x^{k - 1}'
		k -= 1

#print(string)


# Проверка на наличие коэффициентов = 0 

nums = []
nums = string.split('+')

nums1 = []

for i in range(len(nums)): 
	if not nums[i].startswith('0'):     
		nums1.append(nums[i])

print(' + '.join(nums1) + ' = 0')