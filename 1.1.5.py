# Start learn python code to 100 tasks https://code.mu/ru/python/tasker/stager/
# Задача 1.1 №5 Даны два слова. Проверьте, что первые буквы этих слов совпадают.
word1 = str(input("Enter a word1: "))
word2 = str(input("Enter a word2: "))

if word1[0] == word2[0]: # проверка символа по индексу // [0] - первый символ [-1] - последний
    print('true')
else:
    print('false')