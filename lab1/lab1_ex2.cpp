#include <iostream>
#include <string>
using namespace std;

class Animal{
public:
    virtual void is_moving() {
       cout << "Animal is moving." << endl;
   }

    virtual void is_eating() {
        cout << " is eating." << endl;
    }
};

class Dog : public Animal{
public:
    string name;
    string breed;
public:
     void is_moving() override {
        cout << "Dog is moving." << endl;
    }
    void is_eating() override {
         cout << "Dog is eating." << endl;
     }
    static void is_barking(const Dog& doggy){
        printf(" %s is barking", doggy.name.c_str());
    }
};

class Cat : public Animal{
public:
    string name;
    string breed;
    void is_moving() override {
        cout << "Cat is moving." << endl;
    }
    void is_eating() override {
        cout << "Car is eating." << endl;
    }
   static void is_meowing(const Cat& kitty) {
       printf("%s is meowing", kitty.name.c_str());
    }
};

int main(){
    Dog my_dog;
    Cat my_cat;
    printf("Dogs name:");
    cin >> my_dog.name;
    printf("Dogs breed");
    cin >> my_dog.breed;
    printf("Cats name:");
    cin >> my_cat.name;
    printf("Cats breed");
    cin >> my_cat.breed;

    Dog::is_barking(my_dog);
    my_dog.is_moving();
    my_dog.is_eating();
    Cat::is_meowing(my_cat);
    my_cat.is_moving();
    my_cat.is_eating();

}
