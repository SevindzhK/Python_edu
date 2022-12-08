#!/usr/bin/env python3
from collections import Counter

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# - Ввод:[1,1,2,4,5,6,7,7,8], результат: [2,4,5,6,8]

numbers = [1,2,2,3,4,5,6,7,7,8]
result = []

for item in Counter(numbers).items():
	if item[1] == 1:
		result.append(item[0])
print(result) 