# Start learn python code to 100 tasks https://code.mu/ru/python/tasker/stager/
# Задача 1.2 №№3  Дано число. Выведите в консоль сумму первой и последней цифры этого числа.



number1 = str(input('введите число:'))
number2 = str(input('введите число:'))



x = number1[0].isdigit()
y = number2[-1].isdigit()

if x and y: # проверка что x и y  is digit


    digit1 = int(number1[0]) # вызываем функцию которая возвращает число
    digit2 = int(number2[-1]) # вызываем функцию которая возвращает число
    print(digit1 + digit2) # складываем числа
else:
    print('это не число')



number3 = str(input('введите число:')) # по аналогии сделано сумма первого и последнего цифры из числа

z = number3[-1].isdigit()
k = number3[0].isdigit()

if z and k:
    digit4 = int(number3[0])
    digit3 = int(number3[-1])

print(digit3 + digit4)

    