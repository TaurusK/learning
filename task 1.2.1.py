# Start learn python code to 100 tasks https://code.mu/ru/python/tasker/stager/
# Задача 1.2 №1  Дано число. Выведите в консоль первую цифру этого числа.
import re

x = str(input("Enter a number: ")) # проблема - тут выводит любой первый символ не только числа
first_x = x[0]
print(first_x)



"""
как подсказывает жпт чат с использованием функции get_first_digit
"""
s = 'asdfg231'
def get_first_digit(s): # Функция перебирает все символы и выводит первую попавшуюся цифру
    for char in s:
        if char.isdigit(): # isdigit == эта цифра
            return char
print(get_first_digit(s))




