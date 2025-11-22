# Start learn python code to 100 tasks https://code.mu/ru/python/tasker/stager/
# Задача 1.2 №5 Даны два числа. Проверьте, что первые цифры этих чисел совпадают.


number1 = str(input('введите число:'))
number2 = str(input('введите число:'))

'''добавить проверку строки на цифры и буквы'''
x = number1[0].isdigit()
y = number2[0].isdigit()
digit1 = int(number1[0])
digit2 = int(number2[0])
if digit1 == digit2: # проверка что число равняеться числу
   print('числа совпадают')
else:
    print('первые числа не совпадают')


