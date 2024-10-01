#include <iostream>
#include <string>
using namespace std;

class Person {
public:
    virtual string getRole() = 0;

    void print_role(){
        cout << "Role: " << getRole() << endl;
    };
};

class Student : public Person {
public:
    string getRole() override {
        return "Student";
    }
};

class Teacher : public Person {
    public:
    string getRole() override {
        return "Teacher";
    }
};

class Administrator : public Person {
    public:
    string getRole() override {
        return "Administrator";
    }
};

int main(){
   Student student;
   Teacher teacher;
   Administrator admin;

   cout << student.getRole()<< "\n";
   cout << teacher.getRole()<< "\n";
   cout << admin.getRole()<< "\n";

   // Polymorphism
   Person* s = new Student();
   s->print_role();
   Person* t = new Teacher();
   t->print_role();
   Person* a = new Administrator();
   a->print_role();

    return 0;
}