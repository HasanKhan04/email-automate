import smtplib
import random
import datetime as dt
import pandas

my_email = "hasankhanalt@gmail.com"
password = "dhavwnvdlocelwei"


now = dt.datetime.now()
today = (now.month, now.day)
data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
for key in birthday_dict:
    if key == today:
        bday_person = birthday_dict[key]
        letter_num = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_num}.txt") as file:
            contents = file.read()
            contents = contents.replace("[NAME]", bday_person["name"])

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=bday_person["email"],
                                msg=f"Subject:Happy Birthday! \n\n{contents}")









# 4. Send the letter generated in step 3 to that person's email address.




