def display_menu():
    print("1) Insert a car")
    print("2) Show car cataloged")
    print("3) Delete a car")
    print("0) Exit the program")


class Car:

    def __init__(self, brand, year, price):
        self.brand = brand
        self.year = year
        self.price = price

    def __str__(self):
        return f"Name: {self.brand}, Year: {self.year}, Price:{self.price}$"


class Catalog:
    def __init__(self):
        self.list = []

    def get_length(self):
        return len(self.list)

    def show_list_of_cars(self):
        if not self.list:
            print("No cars in the list")
        else:
            for i, car in enumerate(self.list):
                print(f"{i + 1}.{car}")

    def delete_car(self, index):
        if not self.list:
            print("No cars in the list")
        else:
            for i, car in enumerate(self.list):
                if i + 1 == index:
                    del self.list[i]
                    print(f"Car {i + 1} deleted successfully")
                    break

    def input_car(self):
        name = input("Car name:")
        year = int(input("Car year:"))
        price = float(input("Car price:"))
        self.list.append(Car(name, year, price))


def main():
    car_catalog = Catalog()

    while True:
        display_menu()
        opt = input()
        if opt == '1':
            car_catalog.input_car()
            print("There are ", car_catalog.get_length(), " cars in the catalog")
        elif opt == '2':
            car_catalog.show_list_of_cars()
        elif opt == '3':
            index = int(input("Enter the number of the car to delete: "))
            car_catalog.delete_car(index)
        elif opt == '0':
            print('Exiting program...')
            break


if __name__ == "__main__":
    main()
