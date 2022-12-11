import random
word_list = ['человек', 'работа', 'вопрос', 'сторона', 'страна', 'случай', 'голова', 'ребенок', 'система',
             'отношение', 'женщина', 'деньги', 'машина', 'проблема', 'решение', 'история', 'власть', 'тысяча',
             'результат', 'область', 'статья', 'компания', 'группа', 'развитие', 'процесс', 'условие',
             'средство', 'начало', 'уровень', 'минута', 'качество', 'дорога', 'действие', 'любовь',
             'взгляд', 'общество', 'президент', 'комната', 'порядок', 'момент',
             'письмо', 'помощь', 'ситуация', 'состояние', 'квартира', 'внимание', 'смерть', 'программа', 'задача',
             'разговор', 'информация', 'положение', 'интерес',
             'правило', 'управление', 'мужчина', 'партия', 'сердце', 'движение', 'материал', 'неделя',
             'чувство', 'газета', 'причина', 'основа', 'товарищ', 'культура', 'данные', 'мнение', 'документ',
             'институт', 'проект', 'встреча', 'директор', 'служба', 'судьба', 'девушка', 'очередь', 'состав',
             'событие', 'объект', 'создание', 'значение', 'период', 'искусство', 'структура', 'пример',
             'гражданин', 'начальник', 'принцип', 'воздух', 'характер', 'борьба',
             'размер', 'образование', 'мальчик', '', 'участие', 'девочка', 'политика', 'картина']

def get_word():
    return random.choice(word_list).upper()
print(get_word())

def display_hangman(tries):
    stages = [
                '''                      ОЙ
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                '''           Это была моя любимая нога...
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                '''               Забрали и вторую :(
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                '''               Теперь ещё и рука...
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                '''                И тело туда же :(
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                '''                 О нет, голова!
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                '''                  Пока никого :)
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

word = get_word()

def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    symbols = '!@#$%^&*()-=+/\\.?,'
    eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print('---Давайте играть в угадайку слов!---')
    print(display_hangman(tries))
    print(word_completion)
    while tries != 0 and guessed == False:
        a = input().upper()
        while a.isalpha() == False or a in symbols or a in guessed_letters or a in guessed_words or a.upper() in eng:
            a = input('Нужно ввести букву или слово на русском языке\nСмотрите, чтобы буквы не повторялись\n').upper()
            print()
        if a in word and len(a) == 1:
            guessed_letters.append(a)
            for i in range(len(word)):
                if word[i] == a:
                    word_completion = word_completion[:i] + a + word_completion[i + 1:]
            print('Отлично! Идём дальше\n')
            print(word_completion)
            if word_completion == word:
                guessed = True
                return print('\nПоздравляем, вы угадали слово! Вы победили!')
        elif a == word:
            guessed = True
            return print('\nПоздравляем, вы угадали слово! Вы победили!')
        elif a != word and len(a) == len(word):
            tries -= 1
            print('Увы, это не то слово. У Вас осталось не так много попыток, всего', tries, '\n')
            print(display_hangman(tries))
            guessed_words.append(a)
        elif a not in word and len(a) == 1:
            guessed_letters.append(a)
            tries -= 1
            print('Увы, такой буквы нет. У Вас осталось не так много попыток, всего', tries, '\n')
            print(display_hangman(tries))

    return print(f'Вы проиграли :(\nЗагаданное слово - {word}')
play(word)