# primes = {2, 3, 5, 7}
# print(primes)

# evens = set([2, 4, 6, 8])
# odds = set((1, 3, 5, 7))
# print(evens)
# print(odds)

# numbers = {1, 2, 3, 2, 3}
# print(f"The length of numbers is {len(numbers)}")

# for number in numbers:
#     print(number)

# favorit_language = {
#     'john': 'python',
#     'jane': 'c',
#     'david': 'rust',
#     'sarah': 'python',
#     'peter': 'c',
#     'michael': 'python'
# }

# for language in favorit_language.values():
#     print(language.title())

# favorit_language = {
#     'john': 'python',
#     'jane': 'c',
#     'david': 'rust',
#     'sarah': 'python',
#     'peter': 'c',
#     'michael': 'python'
# }

# for language in set(favorit_language.values()):
#     print(language.title())

# primes = {2, 3, 5, 7}
# print(primes)

# primes.add(11)
# print(primes)

# primes.remove(2)
# print(primes)

# first_set = {1, 2, 3}
# second_set = {3, 4, 5}

# print(first_set | second_set)
# # print(first_set.union(second_set))

# print(first_set & second_set)
# # print(first_set.intersection(second_set))

# print(first_set - second_set)
# # print(first_set.difference(second_set))

# print(first_set ^ second_set)
# # print(first_set.symmetric_difference(second_set))

# first_set = {1, 2, 3}
# second_set = {3, 4, 5}

# first_set.union(second_set)
# print(first_set)

# first_set.update(second_set)
# print(first_set)

first_set = {1, 2, 3}
second_set = {3, 4, 5}

print(4 in first_set) # False
print(4 in second_set) # True