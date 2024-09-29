#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Book {
public:
    string name;
    string author;

    Book(const string &name_s, const string &author_s) {
        name = name_s;
        author = author_s;
    }
};

class Library {
private:
    vector<Book> list_of_books;

public:
    explicit Library() {
        list_of_books.emplace_back("Bible", "Hesus");
        list_of_books.emplace_back("Ion", "hz cine la scris");
    }

    void display() const {
        for (int i = 0; i < list_of_books.size(); i++) {
            cout << "Name: " << list_of_books[i].name << ", Author: " << list_of_books[i].author << endl;
        }
    }
};

int main() {
    Library library;

    library.display();
    return 0;
}
