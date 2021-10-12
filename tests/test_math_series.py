from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series


def test_version():
    assert __version__ == "0.1.0"


def test_fibonacci0():
    assert fibonacci(0) == 0

def test_fibonacci1():
    assert fibonacci(1) == 1

def test_fibonacci2():
    assert fibonacci(2) == 1

def test_fibonacci3():
    assert fibonacci(3) == 2


def test_lucas0():
    assert lucas(0) == 2

def test_lucas1():
    assert lucas(1) == 1

def test_lucas2():
    assert lucas(2) == 3

def test_lucas3():
    assert lucas(3) == 4


def test_sum_series0_default_values():
    assert sum_series(0) == fibonacci(0)

def test_sum_series1_default_values():
    assert sum_series(1) == fibonacci(1)

def test_sum_series2_default_values():
    assert sum_series(2) == fibonacci(2)

def test_sum_series3_default_values():
    assert sum_series(3) == fibonacci(3)


def test_sum_series0():
    assert sum_series(0,2,1) == lucas(0)

def test_sum_series1():
    assert sum_series(1,2,1) == lucas(1)

def test_sum_series2():
    assert sum_series(2,2,1) == lucas(2)


def test_sum_series3():
    assert sum_series(1,5,4) == 4

def test_sum_series4():
    assert sum_series(2,5,4) == 9

def test_sum_series5():
    assert sum_series(3,3,4) == 11
