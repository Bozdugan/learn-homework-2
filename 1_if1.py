"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
user_age = int(input(
    'Добро пожаловать в 3000 год! Для дальнейшего распределения введите Ваш возраст:  '))


def main(user_age):
    if user_age <= 0:
        return 'Сначала родись, потом пригодись!'
    elif 0 < user_age < 7:
        return 'Самое время отпрвиться в детский сад!'
    elif 7 <= user_age < 18:
        return 'Школа-школа, я скучаюб я скучаю...'
    elif 18 <= user_age < 22:
        return 'Постоянно зажигать, никогда не отдыхать, веселиться-тусовать всю ночь, весь день на пары!'
    elif 22 <= user_age < 65:
        return 'Работа-работа перейди на Федота...'
    else:
        return 'Вас ждет пансионат второе дыхание!'


age = main(user_age)

print(age)
