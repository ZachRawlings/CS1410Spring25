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

def test_div_exception():
    with pytest.raises(ZeroDivisionError):
        div(2,0)

class Calculator:
    def add(self,x,y):
        return x+y
    def sub (self,x,y):
        return x-y
    def mul(self,x,y):
        return x*y
    def div(self,x,y):    
        if y == 0:
            raise ValueError('Can not divide by zero!')
        return x/y

