class Person:
    affiliation = "UVU"
    def __init__(self, name, age, email):
        self. name = name
        self. age = age
        self. email = email
    def __str__(self):
        return (f"{self.name} is associated with {self.affiliation} is {self.age} and their email is {self.email}.")
        
class Student(Person):
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.registered_courses = []
    
    def register_course(self, course):
        self.course = course
        self.registered_courses.append(course)

    def __str__(self):
        courses = ', '.join([course.course_name for course in self.registered_courses])
        return (f"{self.name} is registered for {courses} is {self.age} and their student_id is {self.student_id}.")
    

class Instructor(Person):
    def __init__(self, name, age, email, employee_id, teaching_courses = None):
        super.__init__(name, age, email)
        self.employee_id = employee_id
        if self.teaching_courses == None:
            self.teaching_courses = []
    def __str__(self):
        return (f"{self.name} is teaching {self.teaching_courses} is {self.age} and their employee_id is {self.employee_id}.")
    def add_course(self, course):
        self.course = course
        return self.teaching_courses.append(self.course)

class Employee(Person):
    def __init__(self, name, age, email, employee_id, department):
        super.__init__(name, age, email)
        self.employee_id = employee_id
        self.department = department
    def __str__(self):
        return (f"{self.name} is in the {self.department} department is {self.age} and their employee_id is {self.employee_id}.")



class Course:
    def __init__(self, course_name, course_code, instructor= None, students = None):
        self.course_name = course_name
        self.course_code = course_code
        self.students = students
        if self.students == None:
            self.students = []

    def assign_instructor(self, instructor):
        self.instructor = instructor
        return(self.instructor)

    def add_student(self, students):
        self.students.append(students)
        return(students)

    def __str__(self):
        return(f"{self.course_name} is taught by {self.instructor}. It has {self.students} enrolled and its code is {self.course_code}.")
    

A = Student("zach", 21, "email", "12345")
print(A.__str__())
A.register_course("Biology")
print(A.registered_courses)
print(A.__str__())
courseA = Course("Biology", "Bio101")
courseA.assign_instructor("Dr. Smith")
courseA.add_student("zach")
print(courseA.__str__())