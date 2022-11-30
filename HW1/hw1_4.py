#!/usr/bin/env python3

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

position = input('Enter number of position (from 1 to 4):')
match position:
    case "1":
        print("Point's coordinates: x > 0, y > 0")
    case "2":
        print("Point's coordinates: x < 0, y > 0")
    case "3":
        print("Point's coordinates: x < 0, y < 0")
    case "4":
        print("Point's coordinates: x > 0, y < 0") 
    case _:
    	print('You entered incorrect number')

	
