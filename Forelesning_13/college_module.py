class Student:
    def __init__(self, firstname, lastname, age, student_id):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.student_id = student_id

    def get_description(self):
        return f"The students name is: " \
               f"{self.firstname} {self.lastname}" \
               f", is {self.age} years old with student id: " \
               f"{self.student_id}"


class Person:
    def __init__(self, fornavn, etternavn, alder, jobb):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.alder = alder
        self.jobb = jobb

    def hent_info(self):
        return f"Personens navn er {self.fornavn} {self.etternavn}," \
               f" er {self.alder} år gammel, og jobber som {self.jobb}"