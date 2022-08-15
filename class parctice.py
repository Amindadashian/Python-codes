
from tkinter import SEL_FIRST


class Student:
    def __init__(self,first,last,courses = None):
        self.first_name = first
        self.last_name = last
        if courses == None:
            courses = []
        else:
            self.courses = courses
    def add_course(self,course):
        if  course not in self.courses:
            self.courses.append(course)
        else:
            print(f'{self.first_name} {self.last_name} is alredy\
            enrolled in the {course} course.')
    def remove_course(self,course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f'{course}not found')


courses_1=['python','rails','java']
courses_2=['java','rails','c']
mashrur=Student('mashrur','hossein',courses_1)
john = Student('john','dophi',courses_2)
print(mashrur.first_name,mashrur.last_name,mashrur.courses)
print(john.first_name,john.last_name,john.courses)
mashrur.add_course('C')
john.add_course('C++')
print(mashrur.first_name,mashrur.last_name,mashrur.courses)
print(john.first_name,john.last_name,john.courses)
mashrur.remove_course('rails')
john.remove_course('java')
print(mashrur.first_name,mashrur.last_name,mashrur.courses)
print(john.first_name,john.last_name,john.courses)
