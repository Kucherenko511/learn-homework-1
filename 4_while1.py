"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    greeting = input('Как дела? ')
    while greeting != 'хорошо':
        greeting = input('Как дела? ')
      

    
if __name__ == "__main__":
    hello_user()

def summa(a, b):
    print(f'Ой ща как сложим {a} и {b}')
    return (a + b)