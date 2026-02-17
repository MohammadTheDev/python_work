# import json

# filename = "numbers.json"

# numbers = [2, 3, 5, 7, 11, 13]

# with open(filename, "w") as f:
#     json.dump(numbers, f)

# with open(filename, "r") as f:
#     numbers = json.load(f)

# print(numbers)
# print(type(numbers))


import json

filename = "username.json"

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What's your name? ")

    with open(filename, "w") as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}")

else:
    print(f"Welcome back, {username}")
