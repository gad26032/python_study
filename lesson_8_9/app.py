from random import randint

HANGMAN_PICS = [
    '''
     +---+
         |
         |
         |
        ===''',
    '''
     +---+
     0   |
         |
         |
        ===''',
    '''
     +---+
     0   |
     |   |
         | 
        ===''',
    '''
     +---+
     0   |
    /|   |
         |
        ===''',
    '''
     +---+
     0   |
    /|\  |
         |
        ===''',
    '''
     +---+
     0   |
    /|\  |
    /    |
        ===''',
    '''
     +---+
     0   |
    /|\  |
    / \  |
        ==='''
]

words = 'аист акула бабуин баран барсук бык ' \
        'верблюд волк воробей выдра голубь гусь ' \
        'жаба зебра змея индюк кит кобра козел койот ' \
        'корова кошка кролик крыса курица лама ласка ' \
        'лебедь лев лиса лосось лось лягушка медведь моллюск ' \
        'моль мул муравей мышь норка носорог обезьяна олень орел ' \
        'панда паук питон попугай пума семга скунс собака сова ' \
        'тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'

words_list = words.split()


def get_random_word(user_word_list):
    list_len = len(user_word_list) - 1
    rand_index = randint(0, list_len)
    rand_word = user_word_list[rand_index]
    return rand_word


def print_hello():
    print("Привет дружок, сыграем в игру HANGMAN.")


def print_current_status(mistakes, blanks):
    """
    Выводит статус игрока.

    :param mistakes: Количество ошибок
    :param blanks: строка с угаданными буквами
    :return:
    """
    pic = HANGMAN_PICS[mistakes]
    print(pic)
    print("Угаданные буквы:", blanks)


def get_guess(word, guesses):
    """
    Возвращает букву, введенную игроком. Эта функция проверяет,
    что игрок ввел только одну букву и ничего больше.
    :param word: Слово которое надо угадать
    :param guesses: буквы которые были введены ранее.
    :return:
    """
    # word = акула
    # guesses = ['a']
    # guess = b
    while True:
        guess = input("Введите букву:")
        guess = guess.lower()
        if len(guess) != 1:
            print('Вы ввели больше одной буквы. Вы можете ввести только одну букву.')
            print('Попробуйте еще раз.')
        elif guess in guesses:
            print('Вы уже называли эту букву. Назовите другую.')
        elif guess not in 'абвгдеежзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ.')
        else:
            return guess


def main():
    print_hello()
    random_word = get_random_word(words_list)
    mistakes = 0
    blanks = '_' * len(random_word)
    print_current_status(mistakes, blanks)


