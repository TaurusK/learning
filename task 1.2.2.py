# Start learn python code to 100 tasks https://code.mu/ru/python/tasker/stager/
# Задача 1.2 №2 Дано число. Выведите в консоль последнюю цифру этого числа.


def get_last_digit(number):
    return abs(number) % 10  # Берем модуль числа и делим на 10

number = int(input('введите число:'))
print(get_last_digit(number))  # великий ЖПт чат помог не работает с числами 0 < x < 1
