#include <iostream>
#include <string>
#include <vector>
using namespace std;

void show_menu(){
    printf("1. Add student\n");
    printf("2. Show students\n");
    printf("0. Exit\n");

}
class Student{
private :
    string name;
    int age;
public :
    Student(const string& student_name, int student_age) {
    name = student_name;
    age = student_age;
}
    static string get_name(Student index){
        return index.name;
    }
    static int get_age(Student index){
        return index.age;
    }
};

int main(){
    vector<Student> students;
    int choice;
    do{
        show_menu();
        cin >> choice;
        switch(choice){
            case 1: {
                string name;
                int age;
                printf("Student name:");
                cin >> name;
                printf("Student age:");
                cin >> age;
                students.push_back(Student(name, age));
                break;
            }
            case 2:{
                for (int i = 0; i < students.size(); i++) {
                    cout << "Name: " << students[i].get_name(students[i]) << ", Age: " << students[i].get_age(students[i]) << endl;
                }
                break;
            }
            case 0:
                cout << "Exiting..." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }

    }while(choice != 0);
}