# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"I have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")


# describe_pet("hamster", "harry")


# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"I have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")


# describe_pet(pet_name="willie", animal_type="dog")


# def describe_pet_default(pet_name, animal_type="dog"):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")


# describe_pet_default(pet_name="willie")
# describe_pet_default(pet_name="harry", animal_type="hamster")


# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     print(toppings)

#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza(12, "mushrooms", "green peppers", "extra")


def build_profile(first, last, **user_info):
    """Build a dictionary containing we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "albert", "enistein", location="princeton", field="physics", iq=160
)

print(user_profile)