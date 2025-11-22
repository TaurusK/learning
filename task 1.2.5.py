# Start learn python code to 100 tasks https://code.mu/ru/python/tasker/stager/
# Задача 1.2 №5 Даны два числа. Проверьте, что первые цифры этих чисел совпадают.


number3 = str(input('введите число:'))
'''добавить проверку строки на цифры и буквы'''
x = number3[0].isdigit()

if x:
   digit1 = int(number3)
   print(len(number3))
else:
    print('тут есть буквы')


"""if z:
    digit3 = int(number3[])
        print(len(digit3)"""