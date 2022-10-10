print("-----------------------------")

'''
import college_module

college_module.Student
'''

from college_module import Student

student_1 = Student("Ola", "Nordmann", 25, 123456)
print(student_1.firstname)
print(student_1.lastname)
print(student_1.age)
print(student_1.student_id)

print("-----------")

student_2 = Student("Kari", "Nordmann", 26, 654321)
print(student_2.firstname)
print(student_2.lastname)
print(student_2.age)
print(student_2.student_id)

print("-----------------------------")

print(student_1.age)
student_1.age = 28                                  #kan endres!
print(student_1.age)

print("-----------------------------")

print(student_1.get_description())                  #Henter metoden get_description fra modulen
print("--------")
print(student_2.get_description())
