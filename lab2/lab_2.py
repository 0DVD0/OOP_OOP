from Menu import print_main_menu, general_menu, faculty_menu
from functions import load_state, save_state


def main():
    faculties = load_state('faculties.txt')
    while True:
        print_main_menu()
        choice_mm = input("Enter your choice: ")
        if choice_mm == '1':
            general_menu(faculties)
        elif choice_mm == "2":
            faculty_menu(faculties)
        elif choice_mm == "0":
            save_state(faculties)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


while __name__ == "__main__":
    main()
