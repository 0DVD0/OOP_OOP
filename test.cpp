#include <iostream>
#include <string>
using namespace std;

class Person {
public:
    string name;
    int age;

    Person(const string& name_p, int age_p) {
        name = name_p;
        age = age_p;
    }

    void display_person_info() const {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
    }
};

class Student : public Person {
public:
    int id;
    string faculty;

    Student(const string& name_p, int age_p, int id_p, const string& faculty_p)
            : Person(name_p, age_p), id(id_p), faculty(faculty_p) {}

    void display_student_info() const {
        Person::display_person_info();
        cout << "ID: " << id << ", Faculty: " << faculty << endl;
    }
};

class Employee {
public:
    string employeeID;
    string company;

    // Correct constructor
    Employee(const string& emp_id, const string& emp_company)
            : employeeID(emp_id), company(emp_company) {}

    void display_employee_info() const {
        cout << "Employee ID: " << employeeID << endl;
        cout << "Company: " << company << endl;
    }
};

class StudentEmployee : public Student, public Employee {
public:
    // Constructor for StudentEmployee, initializing both Student and Employee
    StudentEmployee(const string& person_name, int person_age, int student_id, const string& student_faculty,
                    const string& emp_id, const string& emp_company)
            : Student(person_name, person_age, student_id, student_faculty),
              Employee(emp_id, emp_company) {}

    // Method to display all information (Person + Student + Employee)
    void display_info() const {
        display_person_info();       // From Person class
        display_student_info();      // From Student class
        display_employee_info();     // From Employee class
    }
};

int main() {
    StudentEmployee student_employee("John", 22, 123456, "Computer Science", "E78910", "Tech Corp");

    student_employee.display_info();

    return 0;
}
