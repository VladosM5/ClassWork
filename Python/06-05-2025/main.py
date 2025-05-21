# students = ['Иван', 'Олег', 'Катя', 'Виктор']
# print(students[0]) # выводит элемент списка по индексу (первый = 0)
# print(students[len(students)-1])
#
# for i in range(len(students)): # используется для изменения значений списка
#     students[i] += 'ooooo'
#     print(students[i])
#
# for i in students: # копирует значения списка в переменную
#     print(i)

# задача сделать список, вывести все четные числа (2 варианта решения)

'''
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in num:
    if(i%2==0):
        print(i)


for i in range(len(num)):
    if (num[i]%2==0):
        print(num[i])
'''

# Пользователь вводит число, нужно определить сколько раз это число встречается в списке

'''
num = int(input())
list = [2, 3, 4, 6, 2, 6, 3, 78, 9, 5, 8, 5, 7, 4, 5, 8, 4, 7, 6, 8, 4]
count = 0
for i in list:
    if (i == num): count +=1
print(count)
'''

# ввести число X; вывести X раз случайные числа из списка

'''
list = [2, 3, 4, 6, 2, 6, 3, 78, 9, 5, 8, 5, 7, 4, 5, 8, 4, 7, 6, 8, 4]
count = int(input('введите число: '))
for i in range(count):
    print(list[random.randint(0, len(list)-1)], end=' ')
'''

# вывести все значения списка с конца в начало

'''
list = [2, 3, 4, 6, 2, 6, 3, 78, 9, 5, 8, 5, 7, 4, 5, 8, 4, 7, 6, 8, 4]
for i in range(len(list)-1, -1, -1):
    print(list[i], end=' ')
'''

# Сумма отрицательных чисел

'''
list = [2, 3, -4, 6, 2, 6, -3, 78, 9, 5, -8, 5, 7, 4, -5, 8, 4, -7, 6, 8, 4]
sum1 = 0
for i in range(0, len(list)-1):
    if list[i] < 0:
        sum1 += list[i]
print('Сумма отрицательных чисел:', sum1)
'''

# Сумма четных чисел

'''
list = [2, 3, -4, 6, 2, 6, -3, 78, 9, 5, -8, 5, 7, 4, -5, 8, 4, -7, 6, 8, 4]
sum2 = 0
for j in range(0, len(list)-1):
    if list[j] % 2 == 0:
        sum2 += list[j]
print('Сумма четных чисел:', sum2)
'''

# Сумма нечетных чисел

'''
list = [2, 3, -4, 6, 2, 6, -3, 78, 9, 5, -8, 5, 7, 4, -5, 8, 4, -7, 6, 8, 4]
sum3 = 0
for k in range(0, len(list)-1):
    if not list[k] % 2 == 0:
        sum3 += list[k]
print('Сумма нечетных чисел:', sum3)
'''

# Произведение элементов с индексами кратными 3

'''
list = [2, 3, -4, 6, 2, 6, -3, 78, 9, 5, -8, 5, 7, 4, -5, 8, 4, -7, 6, 8, 4]
for l in range(0, len(list), 3):
    print(list[l])
'''

# -------------------

# list = [2, 3, -4, 6, 2, 6, -3, 78, 9, 5, -8, 5, 7, 4, -5, 8, 4, -7, 6, 8, 4]
# summ_negative = 0
# summ_odd = 0
# summ_even = 0
#
# for i in list:
#     if i % 2 == 0:
#         summ_odd += i
#     else:
#         summ_even += i
#     if i < 0:
#         summ_negative += i

# --------------------



# Произведение элементов между минимальным и максимальным элементом

'''
numbers = [2, 3, -4, 6, 2, 6, -3, 78, 9, 5, -8, 5, 7, 4, -5, 8, 4, -7, 6, 8, 4]
min = numbers[0]
max = numbers[0]
min_index = 0
max_index = 0
for i in range(0, len(numbers)-1):
    if min > numbers[i]:
        min = numbers[i]
        min_index = i
    if max < numbers[i]:
        max = numbers[i]
        max_index = i

if min_index > max_index: min_index, max_index = max_index, min_index

mult = 1
for i in range(min_index + 1, max_index):
    mult *= numbers[i]
print(mult)
'''

# Сумма элементов, находящихся между первым и последним положительными элементами

'''
numbers = [2, 3, -4, 6, 2, 6, -3, 78, 9, 5, -8, 5, 7, 4, -5, 8, 4, -7, 6, 8, 4]
first_index = 0
last_index = 0
for i in range(len(numbers)):
    if numbers[i] > 0:
        first_index = i
        break
for i in range(len(numbers)-1, -1, -1):
    if numbers[i]>0:
        last_index = i
        break

summ = 0
for i in range(first_index+1, last_index):
    summ += numbers[i]
print(summ)
'''