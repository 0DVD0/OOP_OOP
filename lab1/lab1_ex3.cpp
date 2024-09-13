#include <iostream>
#include <string>
#include <vector>
using namespace std;

void show_menu(){
    printf("1. Add person\n");
    printf("2. Show person\n");
    printf("3. Delete person\n");
    printf("0. Exit\n");
}
class Person{
public:
    string name;
    int age;

    Person(const string& person_name, int person_age){
     name = person_name;
     age = person_age;
    }

   ~ Person(){
       printf("Person has been deleted\n");

    }
};

int main(){
    vector<Person> person_list;
    int choice;
    do{
        show_menu();
        cin >> choice;
        switch (choice) {
            case 1: {
                string name;
                int age;
                printf("Person name:");
                cin >> name;
                printf("Person age:");
                cin >> age;
                person_list.emplace_back(name, age);
                break;
            }
            case 2:{
                if(person_list.empty()){
                    cout << "No persons in the list." << endl;
                    break;
                }
                for(int i = 0; i < person_list.size(); i++){
                    cout << "Name: " << person_list[i].name << ", Age: " << person_list[i].age << endl;
                }
                break;
            }
            case 3:
                if(person_list.empty()){
                    printf("No person in the list");
                } else {
                    person_list.pop_back();
                }
                break;
            case 0:
                cout << "Exiting..." << endl;
                break;
                default:
                    printf("Nahui");
        }
    }while (choice != 0);
}