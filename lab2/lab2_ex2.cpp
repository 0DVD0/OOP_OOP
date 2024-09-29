#include <iostream>
#include <string>
#include <vector>
using namespace std;

void show_menu(){
    cout << "1. Add person" << endl;
    cout << "2. Make student" << endl;
    cout << "0. Exit" << endl;
    cout << "Enter your choice: ";
}

class Person {
public:
    string name;
    int age;

    Person(const string& name_p, int age_p){
        name = name_p;
        age = age_p;

    }

    void display_info() const{
        cout << "Name: " << name << ", Age: " << age << endl;
    }
};

class Student : public Person {
public:
    int id;
    string faculty;

    Student(const string& name_p, int age_p, int id_p, const string& faculty_p) : Person(name_p, age_p){
        id = id_p;
        faculty = faculty_p;
    }
    void display_student_info() const {
        Person::display_info();
        cout << "ID: " << id << ", Faculty: " << faculty << endl;
    }
};

class Employee{
public:
   string company_name;
   string speciality;

    Employee(string &company_name_e, string &speciality_e){
        company_name = company_name_e;
        speciality =  speciality_e;
    }

    void display_employee_info() const{
        cout << "Company Name: " << company_name << ", Speciality: " << speciality << endl;
    }
};

class Student_employee : public Employee, public Student{
public:
   int salary;
   bool employed;

    Student_employee(const Employee& company_name_p,Employee &speciality_p, int salary_p, const string& name_p, int age_p, int id_p, const string& faculty_p) : Employee(
            (string &) company_name_p, (string&) speciality_p), Student(name_p, age_p, id_p, faculty_p){
        salary = salary_p;
        employed = true;
    }

     void display_studentemployee_info() const{
        Student::display_student_info();
        Employee::display_employee_info();
        cout << "Salary: " << salary ;
    }

};
int main(){
    vector<Person> persons_list;
    int choice;
    do{
        show_menu();
        cin >> choice;
        switch (choice) {
            case 1: {
                cout << "Enter persons name: ";
                string name;
                cin >> name;
                cout << "Enter persons age: ";
                int age;
                cin >> age;
                Person temp(name, age);
                persons_list.emplace_back(temp);
                temp.display_info();
                break;
            }
            case 2: {
                cout << "Enter the person to make a student: " << endl;
                string name;
                cin >> name;
                if (!persons_list.empty()){
                for (int i = 0; i < persons_list.size(); i++) {
                    if (persons_list[i].name == name) {
                        Student new_student(persons_list[i].name, persons_list[i].age, i + 1, "Faculty of Science");
                        persons_list.erase(persons_list.begin() + i);
                        persons_list.emplace_back(new_student);
                        new_student.display_student_info();
                        break;
                    } else {
                        cout << "Person not found." << endl;
                    }
                }
                } else {
                    cout << "No persons in the list." << endl;
                }
                break;
            }
            case 3: {
                cout << "Enter the name of the student you want to hire:";
                string name;
                cin >> name;
                if (!persons_list.empty()) {
                    for (int i = 0; i < persons_list.size(); i++) {
                        if (persons_list[i].name == name) {
                            cout << "Enter the company name: ";
                            string company_name;
                            cin >> company_name;
                            cout << "Enter the speciality: ";
                            string speciality;
                            cin >> speciality;
                            Employee new_employee(company_name, speciality);
                            Student_employee new_student_employee(new_employee, new_employee, 5000,
                                                                  persons_list[i].name, persons_list[i].age, i + 1,
                                                                  "Faculty of Science");
                            persons_list.erase(persons_list.begin() + i);
                            persons_list.emplace_back(new_student_employee);
                            new_student_employee.display_studentemployee_info();
                            break;
                        }
                    }
                }
                break;
            }
            case 0: {
                cout << "Exiting..." << endl;
                break;
            }
        }
    } while(choice!= 0);
    return 0;
}