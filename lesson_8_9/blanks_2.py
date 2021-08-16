def func(n):
    for i in range(n):
        print(i)


def sum_numbers(a, b):
    s = a + b
    return s


def prepare_string(s, separator):
    return separator.join(s)


def update_blanks(secret_word, letter, blanks):
    for i in range(len(secret_word)):
        if secret_word[i] in letter:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]
    return blanks