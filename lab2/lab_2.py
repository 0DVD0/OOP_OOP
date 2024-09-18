from enum import Enum
from Menu import main_menu, faculty_menu, general_menu
from functions import search_student_by_id, search_faculties_by_field, student_input, faculty_input, print_faculty, \
    assign_student_id, add_student_to_faculty, find_student_to_graduate


def print_study_fields():
    for field in Study_field:
        print(f"{field.value}.{field.name} ")


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
              f"birth: {self.date_of_birth},\n Enrolment Date: {self.enrolment_date}\n")


class Faculty:
    faculty_name = str()
    abbreviation = str()
    students_list = []
    study_field = Study_field

    def __init__(self, faculty_name, abbreviation, study_field):
        self.faculty_name = faculty_name
        self.abbreviation = abbreviation
        self.study_field = study_field

    def add_student(self, student):
        self.students_list.append(student)

    def graduate_student(self, student):
        self.students_list[student].graduate = True

    def display_students(self):
        for student_index in range(len(self.students_list)):
            if not self.students_list[student_index].graduate:
                self.students_list[student_index].print_info()

    def display_graduates(self):
        for student_index in range(len(self.students_list)):
            if self.students_list[student_index].graduate:
                self.students_list[student_index].print_info()


def main():
    faculties = [Faculty]
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            while True:
                general_menu()
                choice_gm = input("Enter your choice: ")
                if choice_gm == "1":
                    faculty_name, faculty_abbreviation = faculty_input()
                    print_study_fields()
                    study_field = input("Enter study field (1-5): ")
                    faculties.append(Faculty(faculty_name, faculty_abbreviation, Study_field(int(study_field))))
                    pass
                elif choice_gm == "2":
                    student_to_search = input("Enter students identification number:")
                    search_student_by_id(student_to_search, faculties)
                elif choice_gm == "3":
                    for faculty in faculties:
                        print_faculty(faculty)
                elif choice_gm == "4":
                    field_to_search = input("Give the field of study: ")
                    search_faculties_by_field(field_to_search, faculties)
                elif choice_gm == "0":
                    break
        elif choice == "2":
            while True:
                faculty_menu()
                choice_fm = input("Enter choice:")
                if choice_fm == "1":
                    new_first_name, new_last_name, new_email, new_enrollment_date, new_birth_day = student_input()
                    new_student_id = assign_student_id(faculties)
                    new_student = Student(new_first_name, new_last_name, new_email, new_enrollment_date, new_birth_day,
                                          new_student_id)
                    faculty_abbreviation = input("Enter the faculty of the student(abbreviation):")
                    add_student_to_faculty(faculties, new_student, faculty_abbreviation)
                elif choice_fm == "2":
                    student_id_to_graduate = input(f"Enter the student's identification number:")
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
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


while __name__ == "__main__":
    main()
