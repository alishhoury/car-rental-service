class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental = float(rental_price_per_day)

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Rental price per day: {self.get_rental_price()}")

    def calculate_rental_cost(self, days):
        return self.get_rental_price() * days

    def get_rental_price(self):
        return self.__rental

    def set_rental_price(self, new_price):
        self.__rental = float(new_price)


class Car(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, seats):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity = seats

    def display_info(self):
        super().display_info()
        print(f"Seats: {self.seating_capacity}")


class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, engine):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine

    def display_info(self):
        super().display_info()
        print(f"Engine Capacity: {self.engine_capacity}cc")


def show_vehicle_info(vehicle):
    vehicle.display_info()


vehicle_type = input("Vehicle type (car/bike): ").lower()
if vehicle_type == "car":
    brand = input("Brand name: ")
    model = input("Car model: ")
    year = input("Manufacture year: ")
    price = input("Rental price per day: ")
    seats = input("Number of seats: ")
    vehicle = Car(brand, model, year, price, seats)
elif vehicle_type == "bike":
    brand = input("Brand name: ")
    model = input("Bike model: ")
    year = input("Manufacture year: ")
    price = input("Rental price per day: ")
    engine = input("Engine capacity: ")
    vehicle = Bike(brand, model, year, price, engine)
else:
    print("Invalid vehicle type")
    exit()

days = int(input("Enter the number of rental days: "))
new_rental_price = input("Enter new rental price per day: ")
vehicle.set_rental_price(new_rental_price)

print("\nVehicle details:")
show_vehicle_info(vehicle)
print(f"Total rental cost for {days} days: {vehicle.calculate_rental_cost(days)}")
