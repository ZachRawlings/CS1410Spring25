def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

@my_decorator
def add(x,y):
    print(x+y)

say_whee()
add(2,3)

def print_function_name(func):
    def wrapper(*args, **kwargs):
        print(f"Function name: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@print_function_name
def abs_ud(a):
    if a>0:
        return a
    else:
        return -a
    
res = abs_ud(-1)
print(res)

