import pytest
from calcpytest import *
def test_add():
    assert add(2,4) == 6
    assert add(2,-3) == -1
    assert add(-2,-3) == -5
    assert add(-2,4) == 2

def test_sub():
    assert sub(2,3) == -1
    assert sub(2,-3) == 5
    assert sub(-2,-3) == 1
    assert sub(-2,3) == -5

def test_mul():
    assert mul(2,3) == 6
    assert mul(2,-3) == -6
    assert mul(-2,-3) == 6

def test_div():
    assert div(2,3) == 2/3
    assert div(2,-3) == 2/-3