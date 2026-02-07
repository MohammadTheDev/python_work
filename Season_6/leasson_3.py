# primes = [2, 3, 5, 7]

# if 5 in primes:
#     print("Yes")
# else:
#     print("No")

# toppings = ["mushrooms", "green peppers", "extra cheese"]

# for topping in toppings:
#     if topping == "green peppers":
#         print("Sorry, we are out of green peppres right now")
#     else:
#         print(f"Adding { topping }.")

# print("\nFinished making your pizza!")

# toppings = []

# if toppings:
#     for topping in toppings:
#         print(f"Adding { topping }.")
#     print(f"Adding { topping }.")
# else:
#     print("\nFinished making your pizza!")

available_toppings = ["mushrooms", "olives", "green peppres", "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")