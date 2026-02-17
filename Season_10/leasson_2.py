# filename = 'programming.txt'

# with open(filename, 'w', encoding='utf-8') as file_object:
#     file_object.write("I love programming.\n")
#     file_object.write("من عاش ساختن بازی های جدید هستم.\n")

# filename = 'programming.txt'

# with open(filename, 'a', encoding='utf-8') as file_object:
#     file_object.write("I also love finding meaning in large datasets.\n")
#     file_object.write("برنامه‌نویسی وب هم بسیار جذاب است.\n")

score = 1500
with open("scores.txt", "w") as f:
    f.write(str(score))
