# def greet_users(names):
#     """Print a simple greeting to each user in the list."""
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)


# usernames = ["hannah", "ty", "margot"]

# greet_users(usernames)


# def print_models(unprinted_designs, completed_models):
#     """
#     Simulate printing each design, until none are left.
#     Move each design to completed_models after printing.
#     """

#     while unprinted_designs:
#         current_design = unprinted_designs.pop()

#         print(f"Printing model: {current_design}")

#         completed_models.append(current_design)


# def show_completed_models(completed_models):
#     """Show all the models that were printed."""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)


# unprinted_designs = ["phone case", "robot pendat", "dodecahedron"]
# completed_modals = []

# print_models(unprinted_designs, completed_modals)

# show_completed_models(completed_modals)

# print("\nOriginal list check:")
# print(f"Unprinted designs: {unprinted_designs}")


unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_modals(unprinted_designs[:], completed_models)

print("\nCheck after sending a COPY:")
print(f"Original unprinted list: {unprinted_designs}")
print(f"Completed models: {completed_models}")
