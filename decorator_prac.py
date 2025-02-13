import time

def show_elapsed_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(result)
        elapsed = time.perf_counter() - start
        print(f'Elapsed time: {elapsed}')
        return result
    return wrapper

@show_elapsed_time
def add(x,y):
    return x+y
    
add(2,3)