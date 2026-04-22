import smtplib
import datetime as dt
import random

my_email = "theephigab@gmail.com"
password= "odtedgojkoclyfwy"

now = dt.datetime.now()
day_week = now.weekday()

with open("quotes.txt", "r") as file:
    quotes = file.readlines()

if day_week == 1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="theephiga04@outlook.com",
                            msg=f"Subject:Monday Motivation\n\n{random.choice(quotes)}.")