#!/usr/bin/env python3

# Создайте программу для игры в "Крестики-нолики".

field = list(range(1,10))

def print_field(field):
    print ("-" * 13)
    for i in range(3):
        print ("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
        print ("-" * 13)

def get_input(player_symbol):
    valid = False
    while not valid:
        player_answer = input("Выберите номер клетки для " + player_symbol+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод! Попробуйте еще ")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(field[player_answer-1]) not in "XO"):
                field[player_answer-1] = player_symbol
                valid = True
            else:
                print ("Эта клетка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9, чтобы сделать ход.")

def check_win(field):
    win_tuple = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_tuple:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False

def main(field):
    count = 0
    win = False
    while not win:
        print_field(field)
        if count % 2 == 0:
            get_input("X")
        else:
            get_input("O")
        count += 1
        if count > 4:
            tmp = check_win(field)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if count == 9:
            print ("Ничья!")
            break
    print_field(field)

main(field)