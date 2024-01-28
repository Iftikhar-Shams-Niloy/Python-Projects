from twilio.rest import Client

with open('my_info.txt','r') as info: # It has been done to keep personal information confidential
    datas = info.readlines()
    for i in range(len(datas)):
        datas[i] = datas[i].strip()
    print(datas)

twilio_account_sid = datas[0]
twilio_account_auth_token = datas[1]
twilio_number = datas[2]
my_phone = datas[3]

client = Client(twilio_account_sid, twilio_account_auth_token)
