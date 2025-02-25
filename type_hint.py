def add(x:int,y:int)->int:   #declaring inputs and the return value as an int but not inforced
    return x+y

print(add(2,3))

def greet(name:str)->None:  #declaring input as a string and return value as None
    print(f"Hello {name}")

greet("John")
greet(1234) 