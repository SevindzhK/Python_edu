#!/usr/bin/env python3


#Игра в 2021 конфету 

def input_num(player): 
	while True:
		num = int(input(f'Ход игрока {player}. Введите число от 1 до 28 включительно: ')) 
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


candy_count = 2021 
player = 1 

while candy_count > 28: 
	print(f'В игре {candy_count} {candy_name(candy_count)}')
	candy_count -= input_num(player) 
	if player == 1:
		player = 2
	else: 
		player = 1 

print(f'Осталось {candy_count} {candy_name(candy_count)}. Победил игрок {player}!')





