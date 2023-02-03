''' Задание 3 (базовое). Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.'''

number = int(input('Введите целое положительное число '))
if number > 0:
    number1 = str(number)
    number2 = number1 + number1
    number3 = number1 + number1 + number1
    result = number + int(number2) + int(number3)
    print(f'Искомое число: {result}')
else:
    print('Вы ввели число, не соответствующее параметрам! Попробуйте ещё.')