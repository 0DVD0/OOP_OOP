def search_student_by_email(email_to_search, faculties):
    for faculty in faculties:
        for student in faculty.students_list:
            if student.email == email_to_search:
                print(
                    f"First Name: {student.first_name}, Last Name: {student.last_name}, Email: {student.email}, "
                    f"Date of birth: {student.date_of_birth}, Enrolment Date: {student.enrolment_date}, "
                    f"Faculty: {faculty.faculty_name}")
            else:
                print("Student does not exist")


def search_faculties_by_field(field_to_search, faculties):
    for faculty in faculties:
        if faculty.study_field == field_to_search:
            print(f"Faculty Name: {faculty.faculty_name}, Abbreviation: {faculty.abbreviation}")


def student_input():
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    email = input("Enter student's email address: ")
    date_of_birth = input("Enter student's date of birth (YYYY-MM-DD): ")
    enrolment_date = input("Enter student's enrolment date (YYYY-MM-DD): ")
    return first_name, last_name, email, date_of_birth, enrolment_date
