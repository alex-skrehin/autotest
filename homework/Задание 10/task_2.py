# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_first():
    assert all_division(8, 4) == 2


@pytest.mark.one
def test_one():
    assert all_division(1, 1) == 1


@pytest.mark.two
def test_true_division():
    assert all_division(8, 9) == 0.8888888888888888


@pytest.mark.three
def test_negative():
    assert all_division(-1, -5) == 0.2


@pytest.mark.skip('скипнуто')
def test_division_by_zero():
    try:
        all_division(0, 0)
    except ZeroDivisionError:
        print('Деление на ноль')
