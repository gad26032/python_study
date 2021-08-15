list_1 = ["Igor", "Vlad", "Dima", "Andrei"]
# 1. Напечатать только те имена которые начинаются с буквы "A"
for i in list_1:
    if i.startswith('A'):
        print(i)
# 2. Напечатать каждое второе имя
for i in list_1[1::2]:
    print(i)
# 3. Напечатать индекс имени "Dima"
list_1.index("Dima")
# 4. Напечатать первое имя в списке
for i in list_1[:1]:
    print(i)
# 5. Напечатать последнее имя в списке
for i in list_1[3:]:
    print(i)
# 6. Напечатать все имена попорядку
for i in list_1:
    print(i)
# 7. Напечатать все именя в обратном порядке
list_1.reverse()
# 8. Напечатать длинну списка
for i in range(len(list_1)):
    print(i)
# 9. Напечатать индекс последнего имени
print(len(list_1[::-1]))
