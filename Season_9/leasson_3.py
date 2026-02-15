# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0  # Default value

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()


# class ElectricCar(Car):
#     """Represent aspect of car, specific to electric vehicles."""

#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class."""
#         super().__init__(make, model, year)


# my_tesla = ElectricCar("tesla", "model s", 2024)
# print(my_tesla.get_descriptive_name())

# # این کد اشتباه است و خطا می‌دهد!
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         pass

# my_tesla = ElectricCar('tesla', 'model s', 2024)
# print(my_tesla.make)  # AttributeError: 'ElectricCar' object has no attribute 'make'


# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0  # Default value

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()


# class ElectricCar(Car):
#     """Represent aspect of car, specific to electric vehicles."""

#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery_size = 40  # New attribute (in kWh)

#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kWh battery.")


# class ElectricCar(Car):
#     """Represent aspect of car, specific to electric vehicles."""

#     def __init__(self, make, model, year, battery_size=75):
#         """Initialize electric car attributes."""
#         super().__init__(make, model, year)
#         self.battery_size = battery_size
#         self.charge_level = 100

#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kWh battery.")

#     def get_range(self):
#         """Calculate and Return the car's range based on battery."""
#         range_miles = self.battery_size * 4 * (self.charge_level / 100)
#         print(f"This car can go about {range_miles:.0f} miles on current charge.")

#     def charge(self):
#         """Charge the battery to full."""
#         self.charge_level = 100
#         print("Battery is now fully charged!")

#     def drive(self, miles):
#         """Drive the car and reduce charge level."""
#         charge_used = (miles / (self.battery_size * 4)) * 100
#         if charge_used <= self.charge_level:
#             self.charge_level -= charge_used
#             self.odometer_reading += miles
#             print(f"Drove {miles} miles. Charge level: {self.charge_level:.1f}%")
#         else:
#             print("Not enough charge for this trip!")


# my_tesla = ElectricCar("tesla", "model 3", 2024, battery_size=82)
# my_tesla.describe_battery()
# my_tesla.get_range()
# my_tesla.drive(100)
# my_tesla.get_range()


# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0  # Default value

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def fill_gas_tank(self):
#         """Fill the gas tank of the car."""
#         print("Filling the gas tank... Done!")


# class ElectricCar(Car):
#     """Represent aspect of car, specific to electric vehicles."""

#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery_size = 75

#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kWh battery.")

#     def fill_gas_tank(self):
#         """Electric cars don't have gas tanks!"""
#         print("This car dosen't need a gas tank!")


# regular_car = Car("toyota", "camry", 2024)
# electric_car = ElectricCar("tesla", "model s", 2024)

# regular_car.fill_gas_tank()
# electric_car.fill_gas_tank()


class Animal:
    """Base class for all animals."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.energy = 100

    def eat(self):
        """All animals can eat"""
        self.energy += 20
        print(f"{self.name} is eating. Energy: {self.energy}")

    def sleep(self):
        """All animals can sleep."""
        self.energy += 30
        print(f"{self.name} is sleeping. Energy: {self.energy}")

    def make_sound(self):
        """Each animal make a different sound."""
        print("Some generic animal sound...")


class Dog(Animal):
    """A dog is an animal."""

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        """Dogs bark!"""
        print(f"{self.name} says: Woof! Woof!")

    def fetch(self):
        """Only dogs can fetch."""
        self.energy -= 10
        print(f"{self.name} is fetching the ball! Energy: {self.energy}")


class Cat(Animal):
    """A cat is an animal."""

    def __init__(self, name, age, indoor=True):
        super().__init__(name, age)

    def make_sound(self):
        """Cats meow!"""
        print(f"{self.name} says: Meow!")

    def scratch(self):
        """Only cats scratch."""
        print(f"{self.name} is scratching the furniture!")


buddy = Dog("Buddy", 3, "Golden Retriever")
whiskers = Cat("Whiskers", 5)

buddy.eat()
whiskers.sleep()

buddy.make_sound()
whiskers.make_sound()

buddy.fetch()
whiskers.scratch()
