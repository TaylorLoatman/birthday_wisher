
import pandas
import random
import datetime as dt
import smtplib

LETTER_NUMBER = [1, 2, 3]
PLACEHOLDER = "[name]"
MY_EMAIL = "tloatmancodes@gmail.com"
MY_PASSWORD = ""

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)
data = pandas.read_csv("birthdays.csv")

day = data["day"]
month = data["month"]
birthdays_dict = {(month, day):data['year'] for (index, data_row) in data.iterrows()}


if (today_month, today_day) in birthdays_dict:
    with open(f"letter_templates/letter_{random.choice(LETTER_NUMBER)}.txt") as letter:
        letter_content = letter.read()
        birthdays_letter = letter_content.replace(PLACEHOLDER, )

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs= ,
            msg=f"Subject:Happy Birthday\n\n{birthdays_letter}"
        )







