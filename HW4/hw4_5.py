#!/usr/bin/env python3

# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)

with open('equation1.txt', 'r', encoding='utf-8-sig') as f:
    text1 = f.read()
with open('equation2.txt', 'r', encoding='utf-8-sig') as f:
    text2 = f.read()

elements1 = text1.split( )
elements2 = text2.split( )

for i in range(len(elements1)):
	if elements1[i].isdigit():
		elements1[i] = str(int(elements1[i]) + int(elements2[i])) 

result = ' '.join(elements1)

with open('result.txt', 'w') as f:
    f.write(result)

