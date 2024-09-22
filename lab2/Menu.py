from modules import Faculty, Student, Study_field
from functions import search_student_by_id, search_faculties_by_field, student_input, \
    assign_student_id, add_student_to_faculty, find_student_to_graduate, faculty_input


def print_main_menu():
    print("Welcome to TUM's student management system: ")
    print("1. General Menu")
    print("2. Faculty Menu")
    print("0. Exit")


def print_study_fields():
    for field in Study_field:
        print(f"{field.value}.{field.name} ")


def general_menu(faculties):
    while True:
        print_general_menu()
        choice_gm = input("Enter your choice: ")
        if choice_gm == "1":
            faculty_name, faculty_abbreviation = faculty_input()
            print_study_fields()
            study_field = input("Enter study field (1-5): ")
            faculties.append(Faculty(faculty_name, faculty_abbreviation, Study_field(int(study_field))))
        elif choice_gm == "2":
            student_to_search = input("Enter students identification number:")
            search_student_by_id(student_to_search, faculties)
        elif choice_gm == "3":
            for faculty in faculties:
                faculty.print_faculty()
        elif choice_gm == "4":
            print_study_fields()
            field_to_search = input("Give the field of study(1-5): ")
            search_faculties_by_field(int(field_to_search), faculties)
        elif choice_gm == "0":
            break


def faculty_menu(faculties):
    while True:
        print_faculty_menu()
        choice_fm = input("Enter choice:")
        if choice_fm == "1":
            new_first_name, new_last_name, new_email, new_enrollment_date, new_birth_day = student_input()
            new_student_id = assign_student_id(faculties)
            new_student = Student(new_first_name, new_last_name, new_email, new_enrollment_date,
                                  new_birth_day,
                                  new_student_id)
            faculty_abbreviation = input("Enter the faculty of the student(abbreviation):")
            add_student_to_faculty(faculties, new_student, faculty_abbreviation)
        elif choice_fm == "2":
            student_id_to_graduate = input("Enter the student's identification number:")
            find_student_to_graduate(faculties, student_id_to_graduate)
        elif choice_fm == "3":
            for faculty in faculties:
                print(f"Faculty: {faculty.faculty_name.upper()}")
                faculty.display_students()
        elif choice_fm == "4":
            for faculty in faculties:
                print(f"Faculty: {faculty.faculty_name.upper()}")
                faculty.display_graduates()
        elif choice_fm == "0":
            break


def print_general_menu():
    print("1. Add New Faculty")
    print("2. Search Student and Show Faculty")
    print("3. Display Faculties")
    print("4. Display Faculties by Fields")
    print("0. Exit General Menu")


def print_faculty_menu():
    print("1. Create Student")
    print("2. Graduate Student")
    print("3. Display enrolled Students")
    print("4. Display graduated Students")
    print("0. Exit Faculty Menu")


def student_menu():
    print("1. View Student Details")
    print("2. Update Student Details")
    print("3. Delete Student")
    print("0. Exit Student Menu")
