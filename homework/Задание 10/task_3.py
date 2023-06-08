# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("x, y, result", [pytest.param(8, 4, 2, marks=pytest.mark.smoke),
                                          (1, 1, 1),
                                          (8, 9, 0.8888888888888888),
                                          (-1, -5, 0.2),
                                          pytest.param(0, 0, 0, marks=pytest.mark.skip("Скипнутый"))])
def test_one(x, y, result):
    assert all_division(x, y) == result
