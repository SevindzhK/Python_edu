#!/usr/bin/env python3

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Cжатие данных

data = 'AAAABBBCCCCCCDDFFFFFCCCAEEE'

def pack(data):

	result = '' 
	count = 1
	
	for i in range(len(data)):
	
		if i == len(data) -1:
			result += str(count) + data[i] 
			break
		if data[i] == data[i + 1]:
		    count += 1
		else:    
			result += str(count) + data[i]
			count = 1
	return result


   

# Распаковка данных


def unpack(string):

	i = 0
	result = ''
	while i < len(string):
		result += string[i +1] * int(string[i])
		i += 2 
	return result

print(data)
print(pack(data))
print(unpack(pack(data)))