import doctest
def add(a,b):
    '''
    this function adds two numbers
    >>> add(2,3)
    5
    >>> add(2,-3)
    -1
    '''
    return a+b

def factorial(n):
    '''
    This function calculates the factorial of a number
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    '''
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    


if __name__ == "__main__":
    doctest.testmod(verbose=True)
    print(factorial(5))