# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print(f"\nMaking a {size}-inch pizza with the following toopings: ")

#     for topping in toppings:
#         print(f"- {topping}")


# make_pizza(16, "pepperoni")

# make_pizza(12, "mushrooms", "green peppers", "extra chese")


# def build_profile(first, last, **user_info):
#     """Build a dictionnary containing everything we know about user."""
#     user_info["first_name"] = first
#     user_info["last_name"] = last

#     return user_info


# user_profile = build_profile(
#     "albert", "einstein", location="princeton", field="physics")

# print(user_profile)


def main_function(a, b, *args, **kwargs):
    print(f"a= {a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")


main_function(1, 2, 3, 4, name="ali", age=20)
