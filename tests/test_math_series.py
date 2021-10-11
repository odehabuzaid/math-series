from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series


def test_version():
    assert __version__ == "0.1.0"


def test_fibonacci(number: int):
    """
    Test the fibonacci function
    """
    if number == 0:
        assert fibonacci(number) == 0
    elif number == 1 or number == 2:
        assert fibonacci(number) == 1
    elif number == 3:
        assert fibonacci(number) == 2
    elif number == 4:
        assert fibonacci(number) == 3
    elif number == 5:
        assert fibonacci(number) == 5
    elif number == 6:
        assert fibonacci(number) == 8
    elif number == 7:
        assert fibonacci(number) == 13

def test_lucas(number: int):
    if number == 0:
        assert lucas(number) == 0
    elif number == 1 or number == 2:
        assert lucas(number) == 1
    elif number >= 3:
        assert lucas(number) == number - 1
    


def test_sum_series(number: int, f: int = 1, s: int = 2):
    if f == 1 and s == 2:
        assert sum_series(number) == fibonacci(number)
    elif f == 2 and s == 1:
        assert sum_series(number) == lucas(number)


for i in range(0, 7):
    test_fibonacci(i)
    # test_lucas(i)
    # test_sum_series(i)
    # test_sum_series(i, 2, 1)
