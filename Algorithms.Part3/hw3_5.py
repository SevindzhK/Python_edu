#!/usr/bin/env python3

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи)
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]  

number = int(input('Enter a number: '))

fib = [0, 1]
for i in range(2,number + 1): 
	fib.append(fib[i-1] + fib[i-2]) 
	

for j in range(number): 
	fib.insert(0, (fib[1] - fib[0]))    
print(fib)

