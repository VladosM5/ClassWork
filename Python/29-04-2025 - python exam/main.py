#Задание 1

'''
user = int(input('Введите год своего рождения: '))
if 1925 <= user < 1944:
    print('молчаливое поколение')
elif 1944 <= user < 1967:
    print('поколение бэби-бумеров')
elif 1967 <= user < 1984:
    print('поколение Х')
elif 1984 <= user < 2000:
    print('поколение Y — миллениалы')
elif 2000 <= user < 2011:
    print('поколение Z — зуммеры')
elif 2011 <= user:
    print('поколение альфа')
else:
    print('неккоректные данные')
'''

#Задание 2

'''
a = int(input('num1: '))
b = int(input('num2: '))
count = 0
summa = 0
if a > b: a,b = b,a
for i in range(a, b+1):
    if i % 3 == 0:
        count += 1
print()
'''
