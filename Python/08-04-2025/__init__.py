# a = input("введите слово ")
# b = int(input("введите кол-во повторений "))
# print((a+" ")*b)

# n = int(input("до какого числа выводить целые числа? "))
# a = 0
# while a <= n:
#     a = a + 1
#     print(a)

# n = int(input("до какого числа выводить целые числа? "))
# while n >= 0:
#     print(n)
#     n -= 1

# a = int(input("введите число "))
# b = int(input("введите число "))
# if a > b: a,b = b,a
# while a <= b:
#     print(a, end=' ')
#     a += 1

# a = int(input("введите число "))
# b = int(input("введите число "))
# if a > b: a,b = b,a
# while a <= b:
#     print(b, end=' ')
#     a -= 1

# a = int(input('num: '))
# b = 0
# k = 1
# if a < 0: k = -1
# while b!=a:
#     print(b, end=' ')
#     b += k
# print(b)

# a = int(input('num1: '))
# b = int(input('num2: '))
# summa = 0
# if a > b: a,b = b,a
# while a <= b:
#     summa += a
#     a += 1
# print(summa)

# a = int(input('num1: '))
# b = int(input('num2: '))
# if a > b: a,b = b,a
# if a % 2: a += 1
# while a <= b:
#     print(a)
#     a += 2

# a = int(input('num1: '))
# b = int(input('num2: '))
# summa = 0
# if a > b: a,b = b,a
# while a <= b:
#     summa += a
#     a += 1
# print(summa/(b-a))

# x = 0
# n = int(input('ведите число: '))
# while n > 0:
#     a = int(input('введите число: '))
#     if a == 3:
#         x += 1
#     n -= 1
# print(x)

# summa = 0
# n = int(input('количество: '))
# while n > 0:
#     a = int(input())
#     summa += a
#     n -= 1
# print(summa)

# maximum = 0
# n = int(input('количество: '))
# while n > 0:
#     a = int(input())
#     if maximum == 0:
#         maximum = a
#     if maximum < a:
#         maximum = a
#     n -= 1
# print(maximum)

# n = int(input('количество: '))
# s = 0
# while s <= 10:
#     print(f'\t{n}\t * \t{s}\t = {n*s}')
#     s += 1

# n = int(input('введите число: '))
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
# print(factorial)