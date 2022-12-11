import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
num = int(input('Приветствую в генераторе безопасных паролей!\nСколько паролей Вам нужно?\n ---> '))
lenp = int(input('\nХорошо, а какой длины будет пароль?\n ---> '))

digit = input('\nВключать ли цифры "0123456789"?\n (Напишите "да" или "нет")---> ')
if digit.lower() == 'да':
    chars += digits
bigalph = input('\nВключать ли прописные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"?\n (Напишите "да" или "нет")---> ')
if bigalph.lower() == 'да':
    chars += uppercase_letters
smallalph = input('\nВключать ли строчные буквы "abcdefghijklmnopqrstuvwxyz"?\n (Напишите "да" или "нет")---> ')
if smallalph.lower() == 'да':
    chars += lowercase_letters
symbols = input('\nВключать ли символы "!#$%&*+-=?@^_"?\n (Напишите "да" или "нет")---> ')
if symbols.lower() == 'да':
    chars += punctuation
badsymbols = input('\nИсключать ли неоднозначные символы "il1Lo0O"\n (Напишите "да" или "нет")---> ')
if badsymbols.lower() == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_password(lenp, chars):
    password = ''
    for j in range(lenp):
        password += random.choice(chars)
    return password
for _ in range(num):
    print('\n ---> ', generate_password(lenp, chars))