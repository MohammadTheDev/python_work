# registered_users = ["david", "jane", "alice"]

# confirmed_users = []

# while registered_users:
#     current_user = registered_users.pop()

#     print(f"Verifying user: {current_user.title()}")

#     confirmed_users.append(current_user)

# print("\n--- Result ---")
# print(f"Registered (Pending): {registered_users}")
# print(f"Confirmed: {confirmed_users}")


# pets = ["dog", "cat", "goldfish", "cat", "rabbit", "cat"]
# print(f"Original list: {pets}")

# while "cat" in pets:
#     pets.remove("cat")

# print(f"Cleaned list: {pets}")

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Who is the best football player? ")

    responses[name] = response

    repeat = input("Who you like to let another person respond? (yes/no)")
    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} belives the best player in {response.title()}")
