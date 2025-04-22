# raw = int(input('кол-во строк: '))
# column = int(input('кол-во стобцов: '))
#
# for i in range(raw):
#     print('* ' * column)

# raw = int(input('кол-во строк: '))
# column = int(input('кол-во стобцов: '))
# print('* ' * column)
# for i in range(raw-2):
#     print('*'+ ('  ' * (column-2)) + ' *')
# print('* ' * column)

# size = int(input('введите кол-во строк: '))
# for i in range(1, size+1, 1):
#     print(i * '* ')

# size = int(input('введите кол-во строк: '))
# for i in range(size, 0, -1):
#     print(i * '* ')

# size = int(input('введите кол-во строк: '))
# for i in range(1, size+1, 1):
#     print('  ' * (size - i) + '* ' * i)

# size = int(input('введите кол-во строк: '))
# for i in range(0, size+1, 1):
#     print('  ' * (i) + ' *' * (size-i))

'''
*
* *
* * *
* * * *
* * * * *
'''

# size = int(input('введите кол-во строк: '))
# for i in range(0, size+1, 1):
#     for j in range(i):
#         print('*', end=' ')
#     print()

'''
        *
      * *
    * * *
  * * * *
* * * * *
'''

# size = int(input('введите кол-во строк: '))
# for i in range(1, size+1, 1):
#     for j in range(size-i):
#         print(' ', end=' ')
#     for j in range(i):
#         print('*', end=' ')
#     print()

'''
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16
'''

# size = int(input('введите кол-во строк: '))
# count = 1
# for i in range(size):
#     for j in range(size):
#         print(count, end="\t")
#         count += 1
#     print()

'''

   a b c d e f g h
1  * - * - * - * -
2  - * - * - * - *
3  * - * - * - * -
4  - * - * - * - *
5  * - * - * - * -
6  - * - * - * - *
7  * - * - * - * -
8  - * - * - * - *

'''

# symbol = '*'
#
# for i in range(8):
#     for j in range(8):
#         if i%2==j%2:
#             print('* ', end='')
#         else:
#             print('- ', end='')
#     print()

'''
Возведение числа в степень
'''

# a = int(input('введите число: '))
# n = int(input('введите число: '))
# pow = 1
# for i in range(n):
#     pow *= a
# print(pow)