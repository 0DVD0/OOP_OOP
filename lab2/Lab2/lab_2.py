from lab2.Lab2.Menu import print_main_menu, general_menu, faculty_menu
from functions import load_state, save_state
import logging

logging.basicConfig(
    filename='operation_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def main():
    logging.info("Application started")
    faculties = load_state('faculties.txt')
    choice_mm = None
    while choice_mm != '0':
        print_main_menu()
        choice_mm = input("Enter your choice: ")
        logging.info(f"User chose option {choice_mm}")
        if choice_mm == '1':
            general_menu(faculties)
        elif choice_mm == "2":
            faculty_menu(faculties)
        elif choice_mm == "0":
            save_state(faculties)
            logging.info("Application exited, state saved")
            print("Exiting...")
        else:
            logging.warning(f"Invalid choice: {choice_mm}")
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
