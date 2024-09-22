#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>
#include <vector>
using namespace std;

int generate_random_number(){
    srand(time(nullptr));
    int random_number = 100000 + rand() % 900000;
    return random_number;
}


class Student {
    public:
    string first_name;
    string last_name;
    int  student_id;
    int credits;

    Student(string &first_name, string &last_name){
        this->first_name = first_name;
        this->last_name = last_name;
        student_id = generate_random_number();
        credits = 0;
    }
    void add_credit(){
        credits ++;
    }
    void remove_credit(){
        if(credits >= 1){
            credits --;
        } else {
            cout << "Not enough credits to remove." << endl;
        }
    }
    void display_info() const{
        cout << "First Name: " << this->first_name << endl;
        cout << "Last Name: " << this->last_name << endl;
        cout << "Student ID: " << this->student_id << endl;
        cout << "Credits: " << this->credits << endl;
        cout << "-------------------------" << endl;
    }
};

class Faculty {
    public:
    string name;
    vector<Student> faculty_student_list;

    explicit Faculty(string &name){
        this->name = name;
        vector<Student> student_list;
    }

    void add_student(Student &student){
        faculty_student_list.push_back(student);
    }

    Student find_student(int student_id){
        for(int i = 0; i < this->faculty_student_list.size();){
            if(this->faculty_student_list[i].student_id == student_id){
                cout << "Student found";
                return this->faculty_student_list[i];
            }
        }
    }

    void add_credit_student2student(Student &student_1, Student &student_2){
        student_1.credits += student_2.credits;
    }
};
int main() {
vector<Faculty>faculty_list;

int student_id_1;
int student_id_2;
cout << "The id of the student to attribute credits: ";
cin >> student_id_1;
    cout << "The id of the student from who the number of credits will get taken as reference: ";
    cin >> student_id_2;
for (int i = 0; i < faculty_list.size(); i++){
    Student student_1 = faculty_list[i].find_student(student_id_1);
    Student student_2 = faculty_list[i].find_student(student_id_2);
    if(student_1.credits >= 1 && student_2.credits >= 1){
        faculty_list[i].add_credit_student2student(student_1, student_2);
    } else {
        cout << "One of the students does not have enough credits";
    }
}

    return 0;
}
