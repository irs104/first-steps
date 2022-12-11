import random

def is_valid(nrand, num2):
    if 1 <= nrand <= int(num2):
        return True
    else:
        return False

def game():
    print('\nДобро пожаловать в числовую угадайку!')
    num2 = input('Какое число будет пределом в игре?  ---> ')
    nrand = int(random.randint(1, int(num2)))
    c = 1
    while True:
        a = int(input('\nПопробуйте угадать число от 1 до этого предела  --->  '))
        if is_valid(a, num2):
            if a < nrand:
                print('Ваше число МЕНЬШЕ загаданного, давайте еще разок\n')
                c += 1
                continue
            elif a > nrand:
                print('Ваше число БОЛЬШЕ загаданного, давайте еще разок\n')
                c += 1
                continue
            elif int(a) == int(nrand):
                print('\n-----!Вы угадали с', c, 'попытки, поздравляем!-----\n')
                break
        else:
            print('А может быть все-таки введем целое число от 1 до', num2, end='\n')
    print('Спасибо, что играли в числовую угадайку :)\n')
    yn = input('-----Сыграем ещё раз?-----\n(Напишите "да" или "нет")  ---> ')
    if yn.lower() == 'да':
        game()
    elif yn.lower() == 'нет':
        print('\nДо встречи в следующий раз!')
game()