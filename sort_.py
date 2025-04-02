from functools import total_ordering
class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def __str__(self):
        return f"{self.name},{self.age},{self.grade}"
    def __repr__(self):
        return f"{self.name},{self.age},{self.grade}"
    def __eq__(self, other):
        return self.age==other.age
    def __lt__(self, other):
        return self.age<other.age
    
    def combine(obj1, obj2):
        if isinstance(obj1, Student) and isinstance(obj2, Student):
            return Student(obj1.name + obj2.name)
        else:
            return -100
        
class CustomIter:
    def __init__(self):
        self.pos+= 1
        return self
    def __next__(self):
        current = self.pos
        self.pos+= 1
        return current
    
i - CustomIter()
it = i__iter__()

for i in range(10):
    print(next(it))