# Start learn python code to 100 tasks https://code.mu/ru/python/tasker/stager/
# Задача 1.1 №6 Дано слово. Получите его последнюю букву. Если слово заканчивается на мягкий знак, то получите предпоследнюю букву.

word1 = str(input("Enter a word: "))
last_n = word1[-1]
if last_n == 'ь':
    print(word1[-2])
else:
    print(last_n)