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


def get_guess(guesses):
    """
    Возвращает букву, введенную игроком. Эта функция проверяет,
    что игрок ввел только одну букву и ничего больше.
    :param word: Слово которое надо угадать
    :param guesses: буквы которые были введены ранее.
    :return:
    """
    while True:
        guess = input("Введите букву:")
        guess = guess.lower()
        if len(guess) != 1:
            print('Вы ввели больше одной буквы. Вы можете ввести только одну букву.')
            print('Попробуйте еще раз.')
            continue
        elif guess not in 'абвгдеежзийклмнопрстуфхцчшщъыьэюя':
            print(f"Вы ввели символ не из Русского алфавита. Ваша буква: '{guess}'")
            print('Пожалуйста, введите русскую букву.')
            continue
        elif guess in guesses:
            print('Вы уже называли эту букву. Назовите другую.')
            continue
        else:
            return guess


def check_guess(secret_word, user_guess):
    if user_guess in secret_word:
        return True
    else:
        return False


def update_blanks(blanks, letter, secret_word):
    pass


# Сравнить каждую букву в secret_word с letter
# Елси буквы равны то заменить символ под темже индексом в blanks
# что и символ в secret_word буквой из letter
# blanks = '_____'
# letter = 'к'
# secret_word = "акула"
# в резултате blanks должен содержать "_к___"

# 1. найти индекс искомой буквы в secret_wod (index)
# 2. Заменить в blanks пробел под тем же индексом(index) на искомую букву(letter)
# Пример blanks[:3] + "rsitenrti" + blanks[3:]


def main():
    print_hello()
    random_word = get_random_word(words_list)
    mistakes = 0
    blanks = '_' * len(random_word)
    print_current_status(mistakes, blanks)
    user_guesses = list()
    if mistakes >= 6:
        print("Вы проиграли")
    else:
        guess = get_guess(user_guesses)
        user_guesses.append(guess)
        check = check_guess(random_word, guess)
        if check:



