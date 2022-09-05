"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""


def hello_user():
    response = str(input('Как дела? '))
    right_response = 'Хорошо'
    while response != right_response:
        return hello_user()


hello_user()


