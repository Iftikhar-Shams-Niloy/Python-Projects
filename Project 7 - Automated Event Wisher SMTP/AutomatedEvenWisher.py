import datetime as dt
import pandas as pd
import random as rd
import smtplib

def senfMail(event):
    if today in event_dict:
        event_person = event_dict[today]
        letter_directory = 'templates/'+event+str(rd.randint(1,3))+'.txt'

        with open(letter_directory) as letter:
            contents = letter.read()
            contents = contents.replace('[NAME]', event_person['name'])

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(sender, password)
            connection.sendmail(
                from_addr = sender,
                to_addrs = event_person['email'],
                msg= f"Subject:Happy {event}!\n\n{contents}")

sender = 'have.a.niceday.everyday'
password = 'ixri auqu twvq dawg'
get_time = dt.datetime.now()
today =  (get_time.month, get_time.day)

data = pd.read_csv('events.csv')
event_dict = {(value['month'], value['day']): value for (key, value) in data.iterrows()}

if event_dict[today]['event'] == "birthday":
    pass
elif event_dict[today]['event'] == "proposal":
    pass
elif event_dict[today]['event'] == "anniversary":
    pass




