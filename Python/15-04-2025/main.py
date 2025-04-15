# begin = int(input('num1: '))
# end = int(input('num2: '))
# if begin > end: end = end, begin
# while begin <= end:
#     if begin % 4 == 0:
#         print(begin)
#         begin += 4
#     else:
#         begin += 1

# n = int(input())
# counter = 0
# while counter <= n:
#     print(counter)
#     counter += 1

# for i in range(0, 10, 1):
#     print(i, end=' ')
#
# i = 0
# while i < 10:
#     print(i, end=' ')
#     i += 1

'''''Вывод целых чисел от A до B в порядке убывания'''''
# a = int(input('num1: '))
# b = int(input('num2: '))
# if a > b: a,b = b,a
# for i in range(b, a-1, -1):
#     print(i, end=' ')

'''Вывести все четные числа от A до B'''
# a = int(input('num1: '))
# b = int(input('num2: '))
# if a > b: a,b = b,a
# if a % 2: a += 1
# for i in range(a, b + 1, 2):
#     print(i, end=' ')

'''Посчитать сумму всех целых чисел от A до B'''
# a = int(input('num1: '))
# b = int(input('num2: '))
# if a > b: a,b = b,a
# sum = 0
# for i in range(a, b + 1, 1):
#     sum += i
# print(sum)

'''Пользователь вводит число, необходимо посчитать сумму цифр этого числа'''
# a = int(input('num: '))
# sum = 0
# while a:
#     sum += a % 10
#     a = a // 10
# print(sum)

'''Вывести энное кол-во раз слово hello через цикл for'''
# n = int(input())
# for i in range(n):
#     print('hello', end=' ')

'''Нужно ввести N чисел и посчитать их среднеарефметическое'''
# n = int(input())
# sum = 0
# for i in range(n):
#     sum += int(input())
# print(sum / n)

# n = int(input())
# count = 0
# for i in range(n):
#     num = int(input())
#     if num % 2 == 0:
#         count += 1
# print(count)

'''Вывод таблицы умножения'''

# n = int(input())
# for i in range(1, 10):
#     print(n, '*', i, '=', n * i)

'''Рандомные числа'''

# import random
#
# count = 0
# flag = True
# while flag:
#     a = random.randint(10, 99)
#     print('загаданное число', a)
#     # flag = True
#     # while flag:
#     # while count<5:
#         # count += 1
#     for i in range(5):
#         count += 1
#         num = int(input('Введите число: '))
#         if num > a:
#             print('введеное число больше загадонного')
#         elif num < a:
#             print('введеное число меньше загадонного')
#         else:
#             print('УРА!')
#             # flag = False
#             # count = 10
#             break
#     if (count == 5):
#         print('Вы проиграли')
#     print('Вы сделали', count, 'попыток')
#     vibor = input('yes/no: ')
#     if (vibor!='yes'):
#         break