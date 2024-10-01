#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Student {
public:
    string name;
    int age;

    // Constructor using const string& for safety
    Student(const string &name_s, int age_d) : name(name_s), age(age_d) {}
};

class Library {
public:
    string name;
    vector<Student*> students_list;

    // Constructor for Faculty
    Library(const string &name_f, Student *student) : name(name_f) {
        students_list.push_back(student);
    }

    void display() const {
        cout << "Faculty: " << name << endl;
        for (int i = 0; i < students_list.size(); i++) {
            cout << "Name: " << students_list[i]->name << ", Age: " << students_list[i]->age << endl;
        }
    }
};

int main() {
    auto *aladin = new Student("aladin", 19);

    Library fcim("fcim", aladin);

    fcim.display();

    delete aladin;
    aladin = nullptr;
    return 0;
}
