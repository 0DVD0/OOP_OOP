#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>
#include <vector>
using namespace std;


void menu(){
    cout << "1. Add Student" << endl;
    cout << "2. Add credits (student2student)" << endl;
    cout << "3. Find students and add credits " << endl;
    cout << "4. Find students and remove credits" << endl;
    cout << "5. Add faculty" << endl;
    cout << "0. Exit" << endl;
}
int generate_random_number(){

    int random_number = 100000 + rand() % 900000;
    return random_number;
}


class Student {
    public:
    string first_name;
    string last_name;
    int  id;
    int credits;

    Student(string &first_name, string &last_name, int id){
        this->first_name = first_name;
        this->last_name = last_name;
        this->id = id;
        credits = 0;
    }
    void add_credit(int num_to_add){
        for (int i = 0; i < num_to_add; i++) {
            credits++;
        }
    }
    void remove_credit(int num_to_remove){
        if(credits >= 1){
            for(int i = 0; i < num_to_remove; i++){
            credits --;
            }
        } else {
            cout << "Not enough credits to remove." << endl;
        }
    }
    void display_info() const{
        cout << "First Name: " << this->first_name << endl;
        cout << "Last Name: " << this->last_name << endl;
        cout << "Student ID: " << this->id << endl;
        cout << "Credits: " << this->credits << endl;
        cout << "-------------------------" << endl;
    }
};

class Library {
    public:
    string name;
    vector<Student> faculty_student_list;

    explicit Library(string &name){
        this->name = name;
        vector<Student> student_list;
    }

    void add_student(Student &student){
        faculty_student_list.push_back(student);
    }

    void find_student_and_add_credits(int student_id, int credits){
        bool found = false;
        for(int i = 0; i < this->faculty_student_list.size(); i++){
            if(this->faculty_student_list[i].id == student_id){
                cout << "Student found and credits were added\n";
               faculty_student_list[i].add_credit(credits);
               faculty_student_list[i].display_info();
               found = true;
               break;
            }
    }
        if(!found){
            cout << "Student not found.\n";
        }
    }

    void find_student_and_remove_credits(int student_id, int credits){
        bool found = false;
        for(int i = 0; i < this->faculty_student_list.size(); i++){
            if (this->faculty_student_list[i].id == student_id){
                if (this->faculty_student_list[i].credits <= 0){
                faculty_student_list[i].remove_credit(credits);
                faculty_student_list[i].display_info();
                found = true;
                break;
                }
            }
        }
        if(!found){
            cout << "Student not found.\n";
        }
    }
    };


Student find_student(vector<Library> &faculty_list, int student_id){
    for(const auto &faculty : faculty_list) {
        for(const auto &student : faculty.faculty_student_list) {
            if(student_id == student.id){
                return student;
            }
        }
    }
    return Student((string &) "not found", (string &) "not found", 0);
}
void add_credit_student2student(Student &student_1, Student &student_2){
    student_1.credits += student_2.credits;
}
int check_random_number(int id, vector<Library> &faculties){
    bool check = false;
    for(int i=0; i<faculties.size(); i++){
        for(int j=0; j<faculties[i].faculty_student_list.size(); j++){
            if(faculties[i].faculty_student_list[j].id == id){
                check = true;
                return check;
            }
        }
    }
    return check;
}


    int main() {
    srand(time(nullptr));
    vector<Library> faculty_list;
    int choice;
    do {
        menu();
        cout << "Enter choice:";
        cin >> choice;
        switch (choice) {
            case 1:{
                int id;
                bool found = false, check = true;
                string first_name, last_name, faculty;
                cout << "Enter first name: ";
                cin >> first_name;
                cout << "Enter last name: ";
                cin >> last_name;
                  while(check){
                      id = generate_random_number();
                      check = check_random_number(id, faculty_list);
                  }
                cout << "Enter faculty of choice: ";
                cin >> faculty;
                Student student(first_name, last_name, id);
                for (int i = 0 ; i < faculty_list.size() ; i++){
                    if(faculty_list[i].name == faculty){
                        found = true;
                        faculty_list[i].add_student(student);
                        cout << "Student has been added\n";
                        student.display_info();
                        break;
                    }
                }
                if(!found){
                    cout << "Faculty not found\n";
                }
                break;
            }
            case 2:{
                int student_id_1, student_id_2;
                cout << "The id of the student to attribute credits: ";
                cin >> student_id_1;
                cout << "The id of the student from who the number of credits will get taken as reference: ";
                cin >> student_id_2;
                        Student temp_1 = find_student(faculty_list,student_id_1);
                        Student temp_2 = find_student(faculty_list, student_id_2);
                        if ((temp_1.first_name == "not found" & temp_1.last_name == "not found") || (temp_2.first_name == "not found" & temp_2.last_name == "not found")) {
                            cout << "One of the students not found\n";
                            break;
                        } else if (temp_2.credits == 0) {
                            cout << "Student 2 does not have enough credits\n";
                            break;
                        } else if (temp_1.id == student_id_1 && temp_2.id == student_id_2) {
                            add_credit_student2student(temp_1, temp_2);
                            cout << "Credits have been transferred\n";
                            temp_1.display_info();
                            temp_2.display_info();
                            break;
                        }
                break;
            }
            case 3:{
                int student_id_to_search, credits_to_add;
                cout << "Enter students id to increase credits:";
                cin >> student_id_to_search;
                cout << "Enter credits to add:";
                cin >> credits_to_add;
                for (int i = 0; i < faculty_list.size(); i++) {
                    faculty_list[i].find_student_and_add_credits(student_id_to_search, credits_to_add);
                }
                break;
            }
            case 4:{
                int student_id_to_search, credits_to_add;
                cout << "Enter students id to remove credits:";
                cin >> student_id_to_search;
                cout << "Enter credits to remove:";
                cin >> credits_to_add;
                for (int i = 0; i < faculty_list.size(); i++) {
                    faculty_list[i].find_student_and_remove_credits(student_id_to_search, credits_to_add);
                }
                break;
            }
            case 5:{
                string faculty_name;
                cout << "Enter faculty name: ";
                cin >> faculty_name;
                Library faculty(faculty_name);
                faculty_list.push_back(faculty);
                cout << "Faculty has been added\n";
                break;
            }
            case 0:{
                cout << "Exiting..." << endl;
                break;
            }
        }
    }while (choice != 0);
    return 0;
}