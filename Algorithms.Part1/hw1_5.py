#!/usr/bin/env python3 
import math

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

x1 = int(input('Enter x1:'))
y1 = int(input('Enter y1:'))
x2 = int(input('Enter x2:'))
y2 = int(input('Enter y2:'))

distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)

print(format(distance, '.2f'))   
