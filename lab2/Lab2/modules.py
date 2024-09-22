from enum import Enum


class Study_field(Enum):
    MECHANICAL_ENGINEERING = 1
    SOFTWARE_ENGINEERING = 2
    FOOD_TECHNOLOGY = 3
    URBANISM_ARCHITECTURE = 4
    VETERINARY_MEDICINE = 5


class Faculty:
    pass


class Student(Faculty):
    first_name = str()
    last_name = str()
    email = str()
    enrolment_date = int()
    graduate = bool()
    date_of_birth = int()
    student_id = int()

    def __init__(self, first_name, last_name, email, enrolment_date, date_of_birth, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrolment_date = enrolment_date
        self.date_of_birth = date_of_birth
        self.student_id = student_id
        self.graduate = False

    def print_info(self):
        print(f"\n\nFirst Name: {self.first_name},\n Last Name: {self.last_name},\n Email: {self.email},\n Date of"
              f"birth: {self.date_of_birth},\n Enrolment Date: {self.enrolment_date},\n Student ID: {self.student_id}\n")


class Faculty:
    faculty_name = str()
    abbreviation = str()
    students_list = []
    study_field = Study_field

    def print_faculty(self):
        print(f"\nFaculty Name: {self.faculty_name},\n(Abbreviation: {self.abbreviation}),\nNumber of "
              f"students: {len(self.students_list)},\nStudy Field: {self.study_field.name}\n")

    def __init__(self, faculty_name, abbreviation, study_field):
        self.faculty_name = faculty_name
        self.abbreviation = abbreviation
        self.study_field = study_field
        self.students_list = []

    def add_student(self, student):
        self.students_list.append(student)

    def graduate_student(self, student):
        student.graduate = True

    def display_students(self):
        for student_index in range(len(self.students_list)):
            if not self.students_list[student_index].graduate:
                self.students_list[student_index].print_info()

    def display_graduates(self):
        for student_index in range(len(self.students_list)):
            if self.students_list[student_index].graduate:
                self.students_list[student_index].print_info()
