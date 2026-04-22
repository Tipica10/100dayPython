##################### Hard Starting Project ######################
import datetime as dt
import smtplib
import random
import pandas

my_email = "theephigab@gmail.com"
password= "odtedgojkoclyfwy"

#first get hold of the datetime time today in a tuple
today_month = dt.datetime.now().month
today_day = dt.datetime.now().day

today_tuple = (today_month,today_day)
#read csv through pandas and creating dict of tuple: the whole row
data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index,data_row) in data.iterrows()}
#main mistake was having square brackets instead of curly
#I was using today_tuple but that would only say today's date, so i need to create row for month and day as a tuple

if today_tuple in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as template:
        contents = template.read()
        #originally had readlines() as read which is not necessary, not list needed which is why error occurred at replace
        personalised = contents.replace("[NAME]",birthdays_dict[today_tuple]['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthdays_dict[today_tuple]['email'],
                            msg=f"Subject:Happy Birthday!\n\n{personalised}")