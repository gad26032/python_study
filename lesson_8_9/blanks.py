# Сравнить каждую букву в secret_word с letter
# Елси буквы равны то заменить символ под темже индексом в blanks
# что и символ в secret_word буквой из letter

#
# blanks = '_____'
# letter = 'к'
# secret_word = "акула"
# в резултате blanks должен содержать "_к___"

# 1. найти индекс искомой буквы в secret_wod (index)
# 2. Заменить в blanks пробел под тем же индексом(index) на искомую букву(letter)
# Пример blanks[:3] + "rsitenrti" + blanks[3:]
secret_word = "акула"
letter = 'к'
blanks = '_____'
for i in range(len(secret_word)):
    if secret_word[i] in letter:
        blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]
