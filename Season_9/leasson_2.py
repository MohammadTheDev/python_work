# class Car:
#     """A simple attempt represent a car."""

#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0  # Default value

#     def read_odometer(self):
#         """Print a statment showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")


# my_new_car = Car("audi", "a4", 1014)
# my_new_car.read_odometer()


# class BankAccount:
#     def __init__(self, owner_name, account_number):
#         self.owner_name = owner_name
#         self.account_number = account_number
#         self.blance = 0  # موجودی اولیه صفر
#         self.is_active = True  # حساب به صورت پیش فرض فعال است
#         self.transaction_count = 0  # تعداد تراکنش ها


# my_account = BankAccount("Ali Ahmadi", "1234-5678")


# class Car:
#     """A simple attempt represent a car."""

#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0  # Default value

#     def read_odometer(self):
#         """Print a statment showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")


# my_new_car = Car("audi", "a4", 2024)
# my_new_car.read_odometer()

# # Modify an attribute's directly
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()


# class Car:
#     """A simple attempt represent a car."""

#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0  # Default value

#     def read_odometer(self):
#         """Print a statment showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     # def update_odometer(self, mileage):
#     #     """
#     #     Set the odometer reading to the given value.
#     #     Reject the change if it attempts to roll the odometer back.
#     #     """
#     #     if mileage >= self.odometer_reading:
#     #         self.odometer_reading = mileage
#     #     else:
#     #         print("You can't roll back an odometer")

#     # مثال پیشرفته تر با اعتبار سنجی کامل
#     def update_odometer(self, milleage):
#         """Set the odometer reading with full validation."""

#         # بررسی نوع داده
#         if not isinstance(milleage, (int, float)):
#             print("Error: Milleage must be a number!")
#             return

#         # بررسی منفی نبودن
#         if milleage < 0:
#             print("Error: Mileage can not be negative!")
#             return

#         # بررسی عقب نرفتن کیلومتر
#         if milleage < self.odometer_reading:
#             print("You can't roll back an odometer!")
#             return

#         # همه چیز درست است٫ مقدار را تغییر بده
#         self.odometer_reading = milleage


# my_new_car = Car("audi", "a4", 2024)
# my_new_car.read_odometer()
# my_new_car.update_odometer(23_500)
# my_new_car.read_odometer()
# # my_new_car.update_odometer(23_000)


# class Car:
#     """A simple attempt represent a car."""

#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0  # Default value

#     def read_odometer(self):
#         """Print a statment showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject the change if it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer")

# def increment_odometer(self, miles):
#     """Add the given amount to the odometer reading."""
#     if miles >= 0:
#         self.odometer_reading += miles
#     else:
#         print("You can't add negative miles!")


# my_car = Car("toyota", "camry", 2023)
# my_car.update_odometer(15_000)
# my_car.read_odometer()

# my_car.increment_odometer(100)
# my_car.read_odometer()

# my_car.increment_odometer(250)
# my_car.read_odometer()


# # در کلاس حساب بانکلی
# def deposit(self, amount):
#     """Add mony to the account."""
#     if amount > 0:
#         self.blance += amount


# # در کلاس بازیکن
# def add_score(self, points):
#     """Add points to player's score."""
#     if points > 0:
#         self.score += points


# # در کلاس سبد خرید
# def add_item(self, item):
#     """Add an item to the cart."""
#     self.items.append(item)
#     self.item_count += 1


class Car:
    """A simple attempt represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Default value
        self.fuel_level = 100  # ذرصد باک بنزین

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        return f"{self.year}  {self.make} {self.model}".title()

    def read_odometer(self):
        """Print a statment showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Update odometer with validation."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add miles and consum fuel."""
        if miles >= 0:
            self.odometer_reading += miles
            # هر ۱۰ مایل, ۱ درصد بنزین مصرف میشود
            fuel_used = miles / 10
            self.fuel_level = max(0, self.fuel_level - fuel_used)
        else:
            print("You can't add negative miles!")

    def fill_tank(self):
        """Fill the gas tank."""
        self.fuel_level = 100
        print("Tank is now full!")

    def get_status(self):
        """Print the car's current status."""
        print(f"\n--- {self.get_descriptive_name()} ---")
        print(f"Mileage {self.odometer_reading} miles")
        print(f"Fuel level {self.fuel_level} %")


# استفاده از کلاس
my_car = Car("honda", "civic", 2024)
my_car.get_status()

my_car.increment_odometer(150)
my_car.get_status()

my_car.fill_tank()
my_car.get_status()
