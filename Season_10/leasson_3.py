# print("Start of the porogram")

# try:
#     result = 5 / 0
#     print("This line will never execute!")
# except ZeroDivisionError:
#     print("خطا: شما نمی توانید یک عدد را بر صفر تقسیم کنید")

# print("End of the program")


# print("Simple Calculator")
# first_number = input("First number: ")
# second_number = input("Second number: ")

# try:
#     answer = int(first_number) / int(second_number)
# except ZeroDivisionError:
#     print("Error: division on 0 is not possible!")
# except ValueError:
#     print("Error: Please enter the number only")
# else:
#     print(f"Result: {answer}")

# filename = "alice_in_wonderland.txt"

# try:
#     with open(filename, encoding="utf-8") as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f"Sorry, the {filename} it's not find")
#     print("please be sure the file be the right folder")

# def count_words(filename):
#     """Count the approximate number of words in a file."""
#     try:
#         with open(filename, encoding="utf-8") as f:
#             contents = f.read()
#     except FileNotFoundError:
#         print(f"Oops! The file {filename} does not exist.")
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {filename} has about {num_words} words.")


# filenames = ["alice.txt", "siddhartha.txt", "missing_file.txt", "moby_dick.txt"]

# for filename in filenames:
#     count_words(filename)


# def count_words_silently(filename):
#     try:
#         with open(filename, encoding="utf-8") as f:
#             contents = f.read()
#     except FileNotFoundError:
#         # شکست بی‌صدا: کاربر حتی متوجه نمی‌شود خطایی رخ داده
#         pass
#     else:
#         words = contents.split()
#         print(f"File {filename}: {len(words)} words.")

# try:
#     # کد پرخطر
# except:
#     # مدیریت خطا
# finally:
#     # این خط همیشه و همیشه اجرا می‌شود
#     print("Cleaning up resources...")