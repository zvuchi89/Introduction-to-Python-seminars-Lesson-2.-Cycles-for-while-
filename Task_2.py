# Задание 2.
#
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и только арифметические операции.
# Не используйте взятие по индексу.
#
# Пример:
# Ведите целое положительное число: 123456789
# Самая большая цифра в числе: 9

user = int(input('Введите целое положительное число: '))
a = user % 10
user = user // 10
while user > 0:
    if user % 10 > a:
        a = user % 10
        user = user // 10
    print(f' Самая большая цифра в числе: {a}')
    break
else:
    print('Вы ввели неправильное число :( ')
