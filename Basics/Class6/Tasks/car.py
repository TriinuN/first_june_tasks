# Create a class called "Car" with attributes like "make," "model," and "year."
# Create an instance of the Car class and print its attributes.
# Add a method to the Car class that calculates the car's age based on the current year.
# Create a subclass of Car called "ElectricCar" with an additional attribute for battery capacity.
# Override the Car class's method in the ElectricCar subclass to also calculate the remaining battery life.


# Teen klassid
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_attributes(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# auto vanus
    def age(self):
        current_year = 2024
        age = current_year - self.year
        return age


# Elektriautode klass
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

# Aku jääk? kui 2,3% aastas väheneb

    def remaining_battery(self):
        new_battery_capacity = self.battery_capacity * (1 - self.age() * 0.023)
        return new_battery_capacity

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Battery Capacity: {self.battery_capacity}"


# Info auto kohta

car1 = Car("Volvo", "XC90", 2020)
car1.print_attributes()
print("car age:", car1.age())
car2 = ElectricCar("BMW", "i8", 2024,100)
car2.print_attributes()
print("car age:", car2.age())
print("car battery capacity:", car2.remaining_battery())