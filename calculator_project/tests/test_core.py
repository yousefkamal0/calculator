import pytest
from calculator import core

def test_add():
    assert core.add(2, 3) == 5

def test_sub():
    assert core.sub(5, 3) == 2

def test_mul():
    assert core.mul(4, 3) == 12

def test_div():
    assert core.div(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        core.div(1, 0)

def test_power():
    assert core.power(2, 3) == 8
    assert core.power(9, 0.5) == pytest.approx(3.0)
