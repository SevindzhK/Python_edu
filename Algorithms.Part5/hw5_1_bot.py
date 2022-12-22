#!/usr/bin/env python3


#Игра в 2021 конфету 

def input_num(): 
	while True:
		num = int(input(f'Ваш ход. Введите число от 1 до 28 включительно: \n')) 
		if 1 <= num <= 28: 
			return num  
		else: 
			print('Некорректное число!')

def candy_name(n):

	m = n % 10
	match m:
		case 1: return 'конфета' 
		case 2: return 'конфеты'
		case 3: return 'конфеты' 
		case 4: return 'конфеты' 
		case _: return 'конфет' 


candy_count = 72

while candy_count > 28: 
	print(f'В игре {candy_count} {candy_name(candy_count)}')
	candy_count -= input_num() 
	print(f'В игре {candy_count} {candy_name(candy_count)}')
	candy_bot = candy_count % 29 
	candy_count -= candy_bot
	print(f'Ход компьютера: {candy_bot} {candy_name(candy_count)} \n')



print(f'Последние конфеты забрал компьютер, Вы проиграли!')





