import pytest
def add(x,y):
    return x+y

def test_add():
    assert add(2,4) == 6
    assert add(2,-3) == -1
    assert add(-2,-3) == -5
    assert add(-2,4) == 2

if __name__ == "__main__":
    pytest.main()
    print(add(2,3))