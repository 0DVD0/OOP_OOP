from enum import Enum
from Menu import main_menu, faculty_menu, student_menu, general_menu
from functions import search_student_by_email, search_faculties_by_field


class Study_field(Enum):
    MECHANICAL_ENGINEERING = 1
    SOFTWARE_ENGINEERING = 2
    FOOD_TECHNOLOGY = 3
    URBANISM_ARCHITECTURE = 4
    VETERINARY_MEDICINE = 5


def print_study_fields():
    for field in Study_field:
        print(f"{field.value}.{field.name} ")


class Faculty:
    pass


class Student(Faculty):
    first_name = str()
    last_name = str()
    email = str()
    enrolment_date = int()
    graduate = bool()
    date_of_birth = int()

    def __init__(self, first_name, last_name, email, enrolment_date, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrolment_date = enrolment_date
        self.date_of_birth = date_of_birth
        self.graduate = False


class Faculty:
    faculty_name = str()
    abbreviation = str()
    students_list = [Student]
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
        for student in self.students_list:
            if not self.students_list[student].graduate:
                print(
                    f"First Name: {student.first_name}, Last Name: {student.last_name}, Email: {student.email}, Date of "
                    f"birth: {student.date_of_birth}, Enrolment Date: {student.enrolment_date}")

    def display_graduates(self):
        for student in self.students_list:
            if self.students_list[student].graduate:
                print(
                    f"First Name: {student.first_name}, Last Name: {student.last_name}, Email: {student.email}, Date of "
                    f"birth: {student.date_of_birth}, Enrolment Date: {student.enrolment_date}")


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
                    faculty_name = input("Enter faculty name: ")
                    faculty_abbreviation = input("Enter faculty abbreviation: ")
                    print_study_fields()
                    study_field = input("Enter study field (1-5): ")
                    faculties.append(Faculty(faculty_name, faculty_abbreviation, Study_field(int(study_field))))
                    pass
                elif choice_gm == "2":
                    student_to_search = input("Enter students email "
                                              "address:<first_name>.<last_name>@<faculty_abbreviation"
                                              ">.<university_abbreviation>.<contry of"
                                              "university")
                    search_student_by_email(student_to_search, faculties)
                elif choice_gm == "3":
                    for faculty in faculties:
                        print(f"Faculty Name: {faculty.faculty_name}(Abbreviation: {faculty.abbreviation}), Number of "
                              f"students: {len(faculty.students_list)}, Study Field: {len(faculty.study_field)}")

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
                    new_first_name = input("Enter student's first name:")
                    new_last_name = input("Enter student's last name:")
                    new_email = input("Enter student's email address:")
                    new_enrollment_date = input("Enter student's enrollment date:")
                    new_birth_day = input("Enter student's birth day:")
                    new_student = Student(new_first_name, new_last_name, new_email, new_enrollment_date, new_birth_day)
                    fa
                elif choice_fm == "2":
                    pass
                elif choice_fm == "3":
                    pass
                elif choice_fm == "4":
                    pass
                elif choice_fm == "0":
                    break
        elif choice == "3":
            student_menu()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


while __name__ == "__main__":
    main()
