import smtplib

my_email = "have.a.happyday.everyday@gmail.com"
my_password = "ioly ajzw ompe uvvo"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="niloyshams22@gmail.com",
                        msg="Subject:HELLO!\n\n Hello there, have a nice day!")

print("Done!")