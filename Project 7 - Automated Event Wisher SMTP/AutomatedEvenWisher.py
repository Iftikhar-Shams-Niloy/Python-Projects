import datetime as dt
import pandas as pd
import random as rd
import smtplib

def sendMail(event):
    if today in event_dict:
        event_person = event_dict[today]
        letter_directory = 'templates/'+event+str(rd.randint(1,3))+'.txt'
        if event == 'birthday':
            age = str(int(year)-int(event_person['year']))
            with open(letter_directory) as letter:
                contents = letter.read()
                contents = contents.replace('[NAME]', event_person['name'])
                contents = contents.replace('[AGE]', age)
                print(contents)
        else:
            with open(letter_directory) as letter:
                contents = letter.read()
                contents = contents.replace('[NAME]', event_person['name'])
                print(contents)

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(sender, password)
            connection.sendmail(
                from_addr = sender,
                to_addrs = event_person['email'],
                msg= f"Subject:Happy {event}!\n\n{contents}"
            )
            print('SMTP--Mail Sent!')

sender = 'have.a.niceday.everyday'
password = 'ixri auqu twvq dawg'
get_time = dt.datetime.now()
today =  (get_time.month, get_time.day)
# fake_today = (8,21) #testing purpose
year = get_time.year

data = pd.read_csv('events.csv')
event_dict = {(value['month'], value['day']): value for (key, value) in data.iterrows()}

try:
    print("We have someone's "+event_dict[today]["event"]+" today!")
    sendMail('birthday')
except:
    print("NO EVENT TODAY!")




