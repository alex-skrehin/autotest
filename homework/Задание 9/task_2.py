# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime
from pathlib import Path


def func_log(gde_decorator):
    def wrapper(file_log='log.txt'):
        """
        Функция записи реального времени в файл
        :param file_log:
        :return:
        """
        dt = datetime.datetime.now()
        date_correct = dt.strftime('%d.%m %H:%M:%S')
        name_func = gde_decorator.__name__ + ' вызвана ' + date_correct + '\n'
        my_func()
        path = Path('C:\Alex_git\homework\Задание 9').joinpath(file_log)
        file_log = open(path, mode='a', encoding='utf-8')
        file_log.write(name_func)
        file_log.close()

    return wrapper


def my_func():
    """

    :return:
    """
    pass


f = func_log(my_func)
f('gde_decorator.txt')

# Здесь пишем код
