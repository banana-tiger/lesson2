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

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def strings_analyser(string1, string2):
        if not type(string1) == str or not type(string2) == str:
            return [0]
        if string1 == string2:
            return [1]
    #Так как в формулировке задачи не указано слово "иначе" - предполагаю возможность выполнения нескольких условий
        elif len(string1) > len(string2):
            several_checks = [2]
            if not string1 == string2 and string2 == 'learn':
                #several_checks.append(3)
                #for i in several_checks:
                return [2, 3]
            else:
                return [2]
        elif not string1 == string2 and string2 == 'learn':
            return [3] 
        else:
            return [4]
#4 - иной исход
    print(strings_analyser(2, 4))
    print(strings_analyser('python', 'learn'))
    print(strings_analyser('learn', 'learn'))
    print(strings_analyser('learn', 'python'))
    print(strings_analyser(4.20 , "it's time"))
    
if __name__ == "__main__":
    main()
