import random
import os
from modules import Study_field, Student, Faculty


def search_student_by_id(id_to_search, faculties):
    found = False
    for faculty in faculties:
        for student in faculty.students_list:
            if student.student_id == id_to_search:
                print(
                    f"First Name: {student.first_name}, Last Name: {student.last_name}, Email: {student.email}, "
                    f"Date of birth: {student.date_of_birth}, Enrolment Date: {student.enrolment_date}, "
                    f"Faculty: {faculty.faculty_name}")
                found = True
                break
    if not found:
        print("Student does not exist")


def search_faculties_by_field(field_to_search, faculties):
    for faculty in faculties:
        if faculty.study_field.value == field_to_search:
            print(f"Faculty Name: {faculty.faculty_name}, Abbreviation: {faculty.abbreviation}")


def student_input():
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    email = input("Enter student's email address: ")
    date_of_birth = input("Enter student's date of birth (YYYY-MM-DD): ")
    enrolment_date = input("Enter student's enrolment date (YYYY-MM-DD): ")
    return first_name, last_name, email, date_of_birth, enrolment_date


def faculty_input():
    faculty_name = input("Enter faculty's name: ")
    abbreviation = input("Enter faculty's abbreviation: ")
    return faculty_name, abbreviation


def assign_student_id(faculties):
    new_student_id = int()
    for faculty in faculties:
        for student in faculty.students_list:
            if student.student_id == new_student_id or new_student_id == 0:
                new_student_id = random.randint(100000, 999999)
                break
    return new_student_id


def add_student_to_faculty(faculties, new_student, faculty_abbreviation):
    for faculty in faculties:
        if faculty.abbreviation == faculty_abbreviation:
            faculty.add_student(new_student)
            break


def find_student_to_graduate(faculties, student_id_to_graduate):
    for faculty in faculties:
        for student in faculty.students_list:
            if student_id_to_graduate == student.student_id:
                if student.graduate:
                    print("Student has already graduated")
                else:
                    print("Student has graduated!!!")
                    faculty.graduate_student(student)
                break


def save_state(faculties, filename="faculties.txt"):
    with open(filename, "w") as file:
        for faculty in faculties:
            file.write(f"{faculty.faculty_name},{faculty.abbreviation},{faculty.study_field.name}\n")
            for student in faculty.students_list:
                file.write(f"{student.first_name},{student.last_name},{student.email},{student.enrolment_date},"
                           f"{student.date_of_birth},{student.student_id},{student.graduate}\n")
            file.write("END_FACULTY\n")


def load_state(filename="faculties.txt"):
    loaded_faculties = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            faculty = None
            for line in file:
                line = line.strip()
                if line == "END_FACULTY":
                    loaded_faculties.append(faculty)
                    faculty = None
                    continue

                if faculty is None or line.startswith("END_FACULTY"):
                    faculty_name, abbreviation, study_field_name = line.split(",")
                    study_field = Study_field[study_field_name]
                    faculty = Faculty(faculty_name, abbreviation, study_field)
                else:
                    first_name, last_name, email, enrolment_date, date_of_birth, student_id, graduate = line.split(",")
                    student = Student(first_name, last_name, email, int(enrolment_date), int(date_of_birth),
                                      int(student_id))
                    if graduate == "True":
                        student.graduate = True
                    faculty.add_student(student)

    return loaded_faculties
