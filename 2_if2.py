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



def main(str_1, str_2):
    result = int
    if type(str_1) != str or type(str_2) != str:
        result = 0
    elif type(str_1) == str and type(str_2) == str:
        if str(str_1) == str(str_2):
            result = 1
        elif (len(str_1) > len(str_2)) and str_2 != 'learn':
            result = 2
        elif str_1 != str_2 and str_2 == "learn":
            result = 3
        else:
            pass
    return print(result)


if __name__ == "__main__":
    main(11231232, 22334213)
    main('cx', 'cx')
    main("xascs", 'csa')
    main('cascacqcqc', 'learn')