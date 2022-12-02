#!/usr/bin/env python3
from datetime import datetime
from datetime import time

# Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа. (Не используя библиотеки связанные с рандомом) 

print('Введите количество разрядов случайного числа, например, если нужно получить число от 10 до 99, то введите "2". Максимальное количество разрядов: 6') 
num = int(input('Введите количество разрядов: '))

if 7 > num > 0: 
	time = str(datetime.time(datetime.now())) 
	random = int(time[-num : ])
	#print(time)
	print(random)  
else: 
	print("Вы ввели некорректное число")

