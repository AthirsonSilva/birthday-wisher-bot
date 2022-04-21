import pandas as pd
import smtplib
from random import randint
from datetime import datetime

MY_EMAIL = 'myemail@gmail.com'
MY_PASSWORD = 'mypassword'

# HINT 1: Create a tuple from today's month and day using datetime. e.g.
today_tuple = (datetime.now().month, datetime.now().day)

# HINT 2: Use pandas to read the birthdays.csv
data = pd.read_csv('./birthdays.csv')

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

# HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f'letter_templates/letter_{randint(1, 3)}.txt'

    with open(file_path) as letter_file:
        content = letter_file.read()
        content.replace('[NAME]', birthday_person['name'])

    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person['email'],
                            msg=f'Subject:Happy birthday\n\n{content}'
                            )
