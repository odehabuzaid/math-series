from math_series import __version__
from math_series.series import fibonacci, lucas


def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci(number: int):
    if number == 0:
        assert fibonacci(number) == 0
    elif number == 1 or number == 2:
        assert fibonacci(number) == 1
    elif number >= 3:
        assert fibonacci(number) == (number - 1)






def test_lucas(number: int):
    if number == 0:
        assert lucas(number) == 0
    elif number == 1 or number == 2:
        assert lucas(number) == 1
    elif number >= 3:
        assert lucas(number) == (number - 1)



for i in range(0, 11):
    test_fibonacci(i)
    test_lucas(i)
    
