"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую

"""

questions_and_answers = {"Как дела?": "Пойдет", "Ты робот?": "Мне нужна твоя одежда и мотоцикл!"}


def ask_user():
    question = str(input('Пользователь: '))
    question_default = questions_and_answers.keys()
    answer = questions_and_answers.get(question)
    while True:
        if question in question_default:
            return f'Программа: {answer}'
        else:
            return ask_user()


print(ask_user())
# if __name__ == "__main__":
#     ask_user(questions_and_answers)
