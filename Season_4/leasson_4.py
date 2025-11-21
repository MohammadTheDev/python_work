# sequence = [start:stop:step]

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# sub_list = numbers[2:6]
# print(numbers)
# print(sub_list)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# left_sub_list = numbers[:5]
# right_sub_list = numbers[5:]
# print(left_sub_list)
# print(right_sub_list)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# sub_list = numbers[-6:-3]
# print(sub_list)

# sub_list = numbers[:-3]
# print(sub_list)

# sub_list = numbers[-6:]
# print(sub_list)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# sub_list = numbers[6:2:-1]
# print(sub_list)

# text = "Hello, World!"
# substring = text[7:12]
# print(substring)

# cities = ['shiraz', 'tehran', 'isfahan', 'tabriz', 'ahwaz']
# for city in cities[:3]:
#     print(city.title())

# x = 5
# y = x
# print(f"x = { x }")
# print(f"y = { y }")

# my_sports = ['football', 'chess', 'basketball', 'volleyball']
# friend_sports = my_sports
# print(my_sports)
# print(friend_sports)

# friend_sports.append('tennis')
# print(my_sports)

my_sports = ['football', 'chess', 'basketball', 'volleyball'] 
friend_sports = my_sports[:]
print(my_sports)
print(friend_sports)

friend_sports.append('tennis')
print(my_sports)
print(friend_sports)