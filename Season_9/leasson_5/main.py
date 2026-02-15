# from random import randint, choice, shuffle, sample

# dice_roll = randint(1, 6)
# print(f"Dice roll: {dice_roll}")

# players = ["charles", "martina", "michael", "florence"]
# first_up = choice(players)
# print(f"First player: {first_up.title()}")

# cards = ["Ace", "King", "Queen", "Jack", "10"]
# shuffle(cards)
# print(f"Shuffled cards: {cards}")

# lottery_numbers = sample(range(1, 50), 6)
# print(f"Lottery numbers: {lottery_numbers}")


# import random
# import string

# def generate_password(length=12, include_symbols=True):
#     """Generate a random password."""
#     # کاراکترهای مجاز
#     characters = string.ascii_letters + string.digits
#     if include_symbols:
#         characters += string.punctuation

#     # ساخت رمز عبور
#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password

# # تولید چند رمز عبور نمونه
# print("Generated Passwords:")
# print(f"  Simple (8 chars):  {generate_password(8, include_symbols=False)}")
# print(f"  Medium (12 chars): {generate_password(12)}")
# print(f"  Strong (16 chars): {generate_password(16)}")


# from datetime import datetime, date, timedelta

# # ۱. تاریخ و زمان فعلی
# now = datetime.now()
# print(f"Current date and time: {now}")
# print(f"Just the date: {now.date()}")
# print(f"Just the time: {now.time()}")

# # ۲. فرمت‌دهی تاریخ
# formatted = now.strftime("%Y/%m/%d - %H:%M")
# print(f"Formatted: {formatted}")

# # ۳. ساخت یک تاریخ خاص
# birthday = date(1990, 5, 15)
# print(f"Birthday: {birthday}")

# # ۴. محاسبه تفاوت زمانی
# today = date.today()
# age_days = (today - birthday).days
# age_years = age_days // 365
# print(f"Age: {age_years} years ({age_days} days)")


# from datetime import datetime, timedelta

# now = datetime.now()

# # محاسبه تاریخ‌های آینده و گذشته
# tomorrow = now + timedelta(days=1)
# next_week = now + timedelta(weeks=1)
# yesterday = now - timedelta(days=1)
# two_hours_later = now + timedelta(hours=2)

# print(f"Now:            {now.strftime('%Y-%m-%d %H:%M')}")
# print(f"Tomorrow:       {tomorrow.strftime('%Y-%m-%d %H:%M')}")
# print(f"Next week:      {next_week.strftime('%Y-%m-%d %H:%M')}")
# print(f"Yesterday:      {yesterday.strftime('%Y-%m-%d %H:%M')}")
# print(f"In 2 hours:     {two_hours_later.strftime('%Y-%m-%d %H:%M')}")

# # محاسبه روزهای باقی‌مانده تا یک رویداد
# new_year = datetime(2025, 3, 21)  # عید نوروز
# days_until = (new_year - now).days
# print(f"\nDays until Nowruz: {days_until} days")


# import statistics

# ages = [18, 21, 21, 25, 30, 35, 21, 28]
# scores = [85.5, 92.0, 78.5, 88.0, 95.5, 82.0]

# # محاسبات آماری پایه
# print("=== Age Statistics ===")
# print(f"Mean (میانگین):     {statistics.mean(ages)}")
# print(f"Median (میانه):     {statistics.median(ages)}")
# print(f"Mode (نما):         {statistics.mode(ages)}")

# print("\n=== Score Statistics ===")
# print(f"Mean:               {statistics.mean(scores):.2f}")
# print(f"Std Dev (انحراف):   {statistics.stdev(scores):.2f}")
# print(f"Variance (واریانس): {statistics.variance(scores):.2f}")

# import statistics


# def analyze_grades(grades):
#     """Analyze a list of student grades."""
#     print("=" * 40)
#     print("         GRADE ANALYSIS REPORT")
#     print("=" * 40)

#     print(f"Number of students: {len(grades)}")
#     print(f"Highest grade:      {max(grades)}")
#     print(f"Lowest grade:       {min(grades)}")
#     print(f"Average (Mean):     {statistics.mean(grades):.1f}")
#     print(f"Median:             {statistics.median(grades):.1f}")

#     avg = statistics.mean(grades)
#     passing = [g for g in grades if g >= 60]
#     print(f"Passing students:   {len(passing)}/{len(grades)}")
#     print(f"Pass rate:          {len(passing)/len(grades)*100:.1f}%")
#     print("=" * 40)


# class_grades = [85, 92, 78, 55, 88, 95, 62, 73, 81, 45, 90, 68]
# analyze_grades(class_grades)

# import secrets

# secure_token = secrets.token_hex(16)  # ۱۶ بایت = ۳۲ کاراکتر هگز
# print(f"Secure Token (hex): {secure_token}")

# url_token = secrets.token_urlsafe(16)
# print(f"URL-safe Token:     {url_token}")

# random_bytes = secrets.token_bytes(8)
# print(f"Random Bytes:       {random_bytes}")

# options = ["option_a", "option_b", "option_c"]
# secure_choice = secrets.choice(options)
# print(f"Secure Choice:      {secure_choice}")

# import secrets
# from datetime import datetime, timedelta

# def generate_reset_link(user_email):
#     """Generate a secure password reset link."""
#     # تولید توکن امن
#     token = secrets.token_urlsafe(32)

#     # زمان انقضا (۱ ساعت)
#     expires_at = datetime.now() + timedelta(hours=1)

#     # ساخت لینک
#     base_url = "https://example.com/reset-password"
#     reset_link = f"{base_url}?token={token}"

#     print(f"Password reset link for {user_email}:")
#     print(f"  Link: {reset_link}")
#     print(f"  Expires: {expires_at.strftime('%Y-%m-%d %H:%M')}")

#     return token, expires_at

# # استفاده
# generate_reset_link("user@example.com")

# import os

# print(f"Current directory: {os.getcwd()}")
# print(f"Files here: {os.listdir('.')}")

import json

data = {"name": "Ali", "age": 25, "city": "Tehran"}
json_string = json.dumps(data)
print(f"JSON: {json_string}")
