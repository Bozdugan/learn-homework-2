"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""


def hello_user():
    response = str(input('Как дела? '))
    right_response = 'Хорошо'
    while response != right_response:
        try:
            return hello_user()
        except KeyboardInterrupt:
            print('Пока!')
            break



hello_user()

# if __name__ == "__main__":
#     hello_user()
