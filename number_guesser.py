import random

def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100

def is_valid_num():
    while True:
        n = input()
        if is_valid(n):
            return int(n)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')

def sravnenie():
    total = 0
    while True:
        n = is_valid_num()
        if n < rn:
            total += 1
            print('Ваше число меньше загаданного, попробуйте еще разок. Попытка №', total)
        elif n > rn:
            total += 1
            print('Ваше число больше загаданного, попробуйте еще разок. Попытка №', total)
        elif n == rn:
            print(f'Вы угадали c {total+1} попытки, поздравляем!')
            break
    print('Спасибо, что играли в числовую угадайку!')

def new_game():
    ng = input('Хотите продолжить? (д/н)\n')
    if ng in ('да', 'д', 'yes', 'y'):
        game()
    elif ng in ('нет', 'n', 'no', 'н'):
        print('Приходите еще, будем ждать!')
    elif ng not in ('да', 'д', 'yes', 'y', 'нет', 'n', 'no', 'н'):
        print('Напишите д или н, пожалуйста')

def game():
    global rn
    rn = random.randint(1, 100)
    print('Добро пожаловать в числовую угадайку')
    print('Напишите ваше предположение, какое число я загадал')
    sravnenie()
    new_game()


game()