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


questions_and_answers = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Ты поел?": "Еще нет"}


def ask_user(questions_and_answers):
    question = input('Задайте вопрос: ')
    while True:
        print(question)
        if question in questions_and_answers.keys():
            print(questions_and_answers[question])
            question = input('Задай другой вопрос - ')
            continue
        elif question == 'Хватит':
            print('Пока пока')
            break
        else:
            print('Попробуй еще ')

if __name__ == "__main__":
    ask_user(questions_and_answers)
