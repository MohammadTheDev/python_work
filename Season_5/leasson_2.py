# user_1 = {'username': 'alice', 'age': 26, 'is_active': False}

# for key in user_1:
#     print(key)

# user_1 = {'username': 'alice', 'age': 26, 'is_active': False}

# for key in user_1.keys():
#     print(key)

# user_1 = {'username': 'alice', 'age': 26, 'is_active': False}

# for key, value in user_1.items():
#     print(f"{key} is {value}")

# user_1 = {'username': 'alice', 'age': 26, 'is_active': False}

# for key in user_1:
#     print(f"{key} is {user_1[key]}")

# favorit_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python'
# }

# for name, language in favorit_language.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

users = {
    "aenistein": {
        "first": "albert",
        "last": "enistein",
        "location": "princeton",
    },
    "mcurie": {"first": "marie", "last": "curie", "location": "paris"},
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info["location"]
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
