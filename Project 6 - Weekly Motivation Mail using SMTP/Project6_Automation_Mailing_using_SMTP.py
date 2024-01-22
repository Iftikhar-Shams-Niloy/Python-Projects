import smtplib
import datetime as dt
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import random
import socket

socket.getaddrinfo('localhost', 8080)
my_email = "have.a.happyday.everyday@gmail.com"
my_password = "iolyajzwompeuvvo"

receiver_list = ['niloyshams21@gmail.com',
                 'syeda.mahjabin.proma@g.bracu.ac.bd']

def sendMail(receiver):
    select_number=random.randint(0,29)
    img_file_name="quote_img/" + str(select_number+1) + ".png"
    with open('motivationQuotes.txt') as quotes:
        fetch_all = quotes.readlines()
        quote = fetch_all[select_number]
    with open(img_file_name, 'rb') as image:
        quote_image = image.read()
    my_message=MIMEMultipart()
    my_message['Subject']='Have a nice day today.'
    my_message['From']= my_email
    my_message['To']= receiver
    message_text = MIMEText("""Dear Myself,
    I hope you will stay motivated all day today and complete all your task with ease.
    Here is a quote to cheer up yourself.
    """+quote)
    my_message.attach(message_text)
    image = MIMEImage(quote_image)
    my_message.attach(image)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(my_message['From'], my_message['To'], my_message.as_string())
        print("SMTP--mail sent!")

now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)
if day_of_week == 0:
    for emails in receiver_list:
        sendMail(emails)
else:
    print("Not today!")
