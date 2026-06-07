# Day 32
# SMTP: Simple Mail Transfer Protocol

# import smtplib

# my_email = "" # a gmail account of mine
# password = "1122334455!!"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()  # TLS stands for Transport Layer Security
# connection.login(user = my_email, password = password)
# connection.sendmail(
#     from_addr = my_email,
#     to_addrs = "@yahoo.com",
#     msg = "Subject:Hello\n\nThis is the body of my email."
# )
# connection.close()

# OR

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()  
#     connection.login(user = my_email, password = password)
#     connection.sendmail(
#         from_addr = my_email,
#         to_addrs = "@yahoo.com",
#         msg = "Subject:Hello\n\nThis is the body of my email."
#     )

# Datetime module

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
# if year == 2025:
#     print("You are good to go!")
# print(type(now))
# print(year)

# date_of_birth = dt.datetime(year = 2005, month = 8, day = 11)
# print(date_of_birth)

# Motivational Quotes Project

import smtplib
import datetime as dt
import random

MY_EMAIL = "" # a gmail account of mine
MY_PASSWORD = "1122334455!!"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:  # 0 denotes Monday
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = MY_EMAIL,
            msg = f"Subject:Monday Motivation\n\{quote}"
        )