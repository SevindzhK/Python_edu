#!/usr/bin/env python3

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

number = int(input('Enter number: '))

# numbers = []
# for i in range(-abs(number), abs(number) +1):      
# 	numbers.append(i)     
# print(numbers)

# List comprehension
numbers = [i for i in range(-abs(number), abs(number) +1)] 
print(numbers)

multiplication = 1
lines = open('index.txt').read().split('\n')

for line in lines:
  multiplication *= numbers[int(line.encode("ascii","ignore"))]

print(multiplication)