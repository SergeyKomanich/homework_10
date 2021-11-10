"""
Пользователь вводит, отдельно, строку и один символ.
Необходимо выполнить поиск в строке всех вхождений указанного пользователем символа.

Для решения НУЖНО использовать только функцию `find()`(rfind()), операторы `if` и `for`(while).

Простой перебор всех символов, от начала до конца строки,
и сравнение каждого символа с искомым НЕ ЯВЛЯЕТСЯ ПРАВИЛЬНЫМ решением.
"""
"""
word = input('enter: ')
letter_in = input('enter: ')
count = 0
for letter in word:
    if letter == letter_in:
        count = count + 1
print(count)
"""
string_enter = input("Введите предложение: ")
letter = input("Введите букву для поиска: ")
letter_s = -1
count = 0

while True:
    letter_s = string_enter.find(letter, letter_s + 1)
    if letter_s == -1:
        break
    count += 1

print("Количество букв в вашем предложении: ", count)
