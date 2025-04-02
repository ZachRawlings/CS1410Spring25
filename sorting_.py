lst_1 = [(7,"mango"), (2,"orange"), (5,"apple"), (9,"banana")]
d1 = dict(lst_1)
# print(d1)

# result = sorted(lst_1, key = lambda item: item[1])
# print(type(result))
# print(result)

import functools

@functools.total_ordering
class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def __eq__(self, value):
        return self.age==value.age
    
    def __lt__(self, value):
        return self.age<value.age
    def __repr__(self):
        return f"{self.name},{self.age},{self.grade}"
    
students = [Student("Alice", 20, "A"), Student("Bob", 21, "A-"), Student("Adam", 21, "A")]
print(sorted(students, key = lambda item: item.age))