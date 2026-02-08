# while condition:
#     # کد هایی ک باید تکرار شوند
#     # loop body

# number = 1

# while number <= 5:
#     print(number)
#     number += 1

# number = 5

# while number:
#     print(number)
#     number -= 1

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# message = ""

# while message != "quit":
#     message = input(prompt)

#     if message != "quit":
#         print(message)

# prompt = "\nPlease enter the name of city you have visited: "
# prompt += "\n(Enter 'quit' when you are finished.)"

# while True:
#     city = input(prompt)

#     if city == "quit":
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

number = 0

while number < 10:
    number += 1

    if number % 2 != 0:
        continue

    print(number)
