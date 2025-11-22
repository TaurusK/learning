# Start learn python code to 100 tasks https://code.mu/ru/python/tasker/stager/
# Даны два целых числа. Проверьте, что первое число без остатка делится на второе.

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = x % y
if x % y == 0:
    print('x / y деляться нацело')
else:
    print(z)

