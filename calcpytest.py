import pytest
import calctestcase
def add(x,y):
    return x+y
def sub (x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):    
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x/y



if __name__ == "__main__":
    pytest.main()
    print(add(2,3))
    print(sub(2,3))
    print(mul(2,3))
    print(div(2,3))
