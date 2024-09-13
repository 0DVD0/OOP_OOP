#include <iostream>
#include <string>
using namespace std;

void show_menu(){
    printf("1. Add person\n");
    printf("2. Show person\n");
    printf("3. Delete person\n");
    printf("0. Exit\n");
}

class Class_B;

class Class_A{
private:
    int number_1;
    int number_2;
public:
   Class_A(int number_first, int number_second){
    number_1 = number_first;
    number_2 = number_second;
}
    friend class Class_B;
   static void display_private_class_b(Class_B& test);

};

class Class_B{
private:
    string word_1;
    string word_2;
    public:
    Class_B(const string& word_first, const string& word_second){
        word_1 = word_first;
        word_2 = word_second;
    }
    friend class Class_A;
 static void display_private_class_a(Class_A& test){
    cout << "Number_1 in Class_A: " << test.number_1 << endl;
    cout << "Number_2 in Class_A: " << test.number_2 << endl;
}
};

void Class_A::display_private_class_b(Class_B& test){
    cout << "Word_1 in Class_B: " << test.word_1 << endl;
    cout << "Word_2 in Class_B: " << test.word_2 << endl;
}

int main(){
    int number_1, number_2;
    printf("Give a number:");
    cin >> number_1;
    printf("Give another number:");
    cin >> number_2;
    Class_A test_1(number_1, number_2);

    string word_1, word_2;
    printf("Give a word:");
    cin >> word_1;
    printf("Give another word:");
    cin >> word_2;
    Class_B test_2(word_1, word_2);
    printf("Class A access to class B:\n");
    test_1.display_private_class_b(test_2);
    printf("Class B access to class A:\n");
    test_2.display_private_class_a(test_1);

}
