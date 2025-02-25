def add(x:int,y:int)->int:
    return x+y

print(add(5,6))

def greet(name:str)->None:
    return f"Hello {name}"



UserID = NewType('UserID', int)

class Stack[T]:
    def __init__(self)-> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()
    
    def empty(self) -> bool:
        return not self.items

stack = Stack[int]()
stack.push(5)   
