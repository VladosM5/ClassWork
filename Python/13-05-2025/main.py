# list = [2, 3, 4]
# print(list)
# list.append(6)
# print(list)
# list.clear()
# print(list)

# list = [2, 3, 4, 5]
# while True:
#     a = int(input('Выберите действие: (1) добавить элемент, (2) очистить список, (3) показать список, (4) Выход  '))
#     if a == 1:
#         list.append(int(input('Введите значение: ')))
#         print(list)
#     elif a == 2:
#         list.clear()
#         print('Список очищен', list)
#     elif a == 3:
#         print('Сам список:', list)
#     elif a == 4:
#         print('Выход из списка')
#         break

# Кол-во элементов в списке, удаление с конкретной позиции, удаление конкретного элемента, добавление элемента в конкретную позицию,
# разворот в обратном порядке списка, сортировка списка

list = [2, 3, 6, 9, 10, 5, 4, 15]
while True:
    print('''
    1. Добавить значение
    2. Очистить список
    3. Вывести список
    4. Показать кол-во элементов в списке
    5. Удалить элемент с позиции
    6. Удалить конкретный элемент
    7. Добавить элемент в конкретную позицию
    8. Развернуть список в обратном порядке
    9. Отсортировать список
    10. Выход
    ''')
    check = int(input('Выберете действие: '))
    if check == 1:
        num = int(input('Введите значение: '))
        list.append(num)
    elif check == 2:
        list.clear()
        print('Список очищен')
    elif check == 3:
        print(list)
    elif check == 4:
        print(len(list))
    elif check == 5:
        num1 = int(input('Введите номер позиции элемента: '))
        list.pop()
        print(list)
    elif check == 6:
        num2 = int(input('Введите элемент: '))
        list.remove(num2)
        print(list)
    elif check == 7:
        num3 = int(input('Введите позицию перед которой нужно добавить элемент: '))
        num4 = int(input('Введите элемент, который нужно добавить: '))
        list.insert(num3, num4)
        print(list)
    elif check == 8:
        list.reverse()
        print(list)
    elif check == 9:
        list.sort()
        print(list)
    elif check == 10:
        break
    else:
        print('Некорректное значение')