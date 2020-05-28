import os

import pytest
from sqrt import sqrt


@pytest.mark.hoge
def test_sqrt():
    n = 2
    expected = 1.4142
    value = sqrt(n)
    assert expected == round(value, 4), f'sqrt({n})'


def test_neg():
    with pytest.raises(ValueError):
        sqrt(-2)


sqrt_cases = [
    (0, 0, False),
    (1, 1, False),
    (2, 1.4142, False),
    (4, 2, False),
    (-2, 0, True),
]


@pytest.mark.parametrize('n, expected, error', sqrt_cases)
def test_sqrt_cases(n, expected, error):
    if error:
        with pytest.raises(ValueError):
            sqrt(n)
        return

    value = sqrt(n)
    assert expected == round(value, 4), f'sqrt({n})'


is_ci = 'CI' in os.environ


@pytest.mark.skipif(not is_ci, reason='not in the CI environment')
def test_that_requires_ci():
    print('CI test')
