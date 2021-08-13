secretword = 'мир'
letter = ''
blanks = '_' * len(secretword)
word = input("Введите букву")
for i in range(len(secretword)):
    if secretword[i] in letter:
        blanks = blanks[:i] + secretword[i] + blanks[i+1:]