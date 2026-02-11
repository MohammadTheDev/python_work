# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()


# musician = get_formatted_name("jimi", "hendrix")
# print(musician)


# def calculate_area(width, height):
#     """Return the area of a rectangle."""
#     area = width * height
#     return area

# rect_area = calculate_area(5, 10)
# print(f"The area of the rectangle is {rect_area}")

# def get_formatted_name(first_name, last_name, middle_name=""):
#     """Return a full name, neatly formatted."""

#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"

#     return full_name.title()


# musician = get_formatted_name("gimi", "hendrix")
# print(musician)

# musician = get_formatted_name("john", "hooker", "lee")
# print(musician)


# def build_person(first_name, last_name, age=None):
#     """Return a dictionary of information about a person."""
#     person = {"first": first_name, "last": last_name}

#     if age:
#         person["age"] = age

#     return person


# musician = build_person("jimi", "hendrix", age=27)
# print(musician)


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == "q":
        break

    l_name = input("Last name: ")
    if l_name == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
