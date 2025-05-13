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

# list = []
# while True:
#     print('''
#     1. Добавить значение
#     2. Очистить список
#     3. Вывести список
#     4. Показать кол-во элементов в списке
#     5. Удалить элемент с позиции
#     6. Удалить конкретный элемент
#     7. Добавить элемент в конкретную позицию
#     8. Развернуть список в обратном порядке
#     9. Отсортировать список
#     10. Выход
#     ''')
#     check = int(input('Выберете действие: '))
#     if check == 1:
#         num = int(input('Введите значение: '))
#         list.append(num)
#     elif check == 2:
#         list.clear()
#         print('Список очищен')
#     elif check == 3:
#         print(list)
#     elif check == 4:
#         print('Длина списка', len(list))
#     elif check == 5:
#         index = int(input('Введите номер позиции элемента: '))
#         if (index < 0 or index > len(list)):
#             print('Не существующий индекс')
#         else:
#             print(list)
#             num1 = int(input('Введите номер позиции элемента: '))
#             list.pop(num1)
#             print(list)
#     elif check == 6:
#         try:
#             list.remove(num2)
#         except:
#             print('Данное значение отсутствует')
#         print(list)
#         num2 = int(input('Введите элемент: '))
#         list.remove(num2)
#         print(list)
#     elif check == 7:
#         num3 = int(input('Введите позицию перед которой нужно добавить элемент: '))
#         num4 = int(input('Введите элемент, который нужно добавить: '))
#         list.insert(num3, num4)
#         print(list)
#     elif check == 8:
#         list.reverse()
#         print('Список развернут', list)
#     elif check == 9:
#         list.sort()
#         print('Список отсортирован', list)
#     elif check == 10:
#         break
#     else:
#         print('Некорректное значение')

# line = input('Введите строку: ')
# line2 = ''
# for i in line:
#     line2 = i+line2
# print(line2)

# ll = ['2', '4', '7', 9]
# # ss = str(ll)
# # print(ss)

# ss = '5 3 4 2 4 21'
# ll = list(ss)
# ll.reverse()
# ss2 = ''
# for i in ll:
#     ss2 += i
# print(ss2)

# line = input('Введите строку: ')
# count_alpha = 0
# count_digit = 0
# for i in line:
#     if i.isalpha():
#         count_alpha += 1
#     if i.isdigit():
#         count_digit += 1
# print(count_alpha)
# print(count_digit)


# line = input('Введите строку: ')
# symbol = input('Введите искомый символ: ')
# print(line.count(symbol))

# line = input('Введите строку: ')
# symbol = input('Введите строку которую хотите поменять: ')
# symbol2 = input('Введите строку на которую хотите поменять: ')
# print(line.replace(symbol, symbol2))
