"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""


def string_check(a, b):
    if not isinstance(a, str):
        return 0
    if not isinstance(b, str):
        return 0
    if a == b:
        return 1
    elif len(a) > len(b):
        return 2
    elif a != b and b == 'learn':
        return 3


print(string_check(2, 'test'))
print(string_check('test', (5, 6)))
print(string_check('test', 'test'))
print(string_check('test_test', 'test'))
print(string_check('test', 'learn'))
