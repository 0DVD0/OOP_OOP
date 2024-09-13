#include <iostream>
#include <string>
#include <vector>
using namespace std;

void show_menu(){
    cout << "Library Management System" << endl;
    cout << "1. Add Book" << endl;
    cout << "2. Remove Book" << endl;
    cout << "3. Display All Books" << endl;
    cout << "0. Exit" << endl;
    cout << "Enter your choice: ";
}

class Book {
public:
    string title;
    string author;
    int ISBN;

    Book(const string& book_title, const string& book_author, int book_ISBN){
        title = book_title;
        author = book_author;
        ISBN = book_ISBN;
    }
};

class Library{
private:
    vector<Book> book_list;
public:
    void add_book(const string& book_title,const string& book_author,int book_ISBN){
       book_list.emplace_back(book_title,book_author,book_ISBN);
    }
    void delete_book(){
        if (book_list.empty()){
            cout << "No books in the library." << endl;
            return;
        } else {
        book_list.pop_back();
        }
    }
    void display_books(){
       for (int i = 0; i < book_list.size(); i++){
    cout << "Title: " << book_list[i].title << endl;
    cout << "Author: " << book_list[i].author << endl;
    cout << "ISBN: " << book_list[i].ISBN << endl;
    cout << "-----------------------------" << endl;
    }
    }

};

int main(){
    Library library_list;
    int choice;
    do{
        show_menu();
        cin >> choice;
        switch (choice) {
            case 1: {
                cout << "Enter book title: ";
                string title;
                cin >> title;
                cout << "Enter book author: ";
                string author;
                cin >> author;
                cout << "Enter book ISBN: ";
                int ISBN;
                cin >> ISBN;

                library_list.add_book(title,author,ISBN);
                break;
            }
            case 2:
                cout << "Book removed successfully!" << endl;
                library_list.delete_book();
                break;
            case 3:
                cout << "All books in the library:" << endl;
                library_list.display_books();
                break;
            default:
            case 0:
                cout << "Exiting..." << endl;
                break;
        } 
    } while(choice!= 0);
    return 0;
}