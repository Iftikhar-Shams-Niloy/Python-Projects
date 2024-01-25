import requests
from twilio.rest import Client
import smtplib
import socket

def sendMail(articles):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(my_email,my_app_password)
        content ="Subject:Stock Update TESLA\n\n"
        dif, dif_per = getStatus()
        content += f'The stock price update is given below,\n<<< {dif} >>>\n<<< {dif_per} >>>\n ***RELATED NEWS:***\n'
        for news in articles:
            content += news + '\n \n'
        print(content)
        print(type(content))
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver,
                            msg=content.encode('utf-8'))
    print('SMTP--Mail Sent!')

def getStatus():
    if price_difference >0:
        result_txt = '(⬆)' + str(abs(price_difference))
        result_percentage_txt ='(⬆)' + str(price_difference_percentage)+'%'
    elif price_difference == 0:
        result_txt = '(⇋)'+ str(abs(price_difference))
        result_percentage_txt='(⇋)' +  str(price_difference_percentage)+'%'
    else:
        result_txt='(⬇)' + str(abs(price_difference))
        result_percentage_txt='(⬇)' +  str(price_difference_percentage)+'%'
    return result_txt,result_percentage_txt

def getArticles():
    news_params={'apiKey': news_api_key,
                 'qInTitle': company_name,}
    fetch_news_data=requests.get(news_endpoint,params=news_params)
    news_articles=fetch_news_data.json()['articles']
    top_three_news=news_articles[:3]
    data_formatted=[f"Headline: {article['title']}. \nBrief: {article['description']}" for article in top_three_news]
    return data_formatted

socket.getaddrinfo('localhost', 8080)
my_email = "have.a.happyday.everyday@gmail.com"
my_app_password = 'cqsf tdzi msot etbh'
receiver = 'have.a.happyday.everyday@gmail.com'

stock_name = "TSLA"
company_name = "Tesla Inc"

stock_endpoint = 'https://www.alphavantage.co/query'
news_endpoint = 'https://newsapi.org/v2/everything'

API_key = 'UTNM73MMKKBMG8HW'
news_api_key= '5acb2aff352e45c8843cffa6e1fb7de6'
twilio_SID = ''
twilio_AUTH_TOKEN = ''

stock_params = {
    'function':'TIME_SERIES_DAILY',
    'symbol':stock_name,
    'apikey':API_key,}

fetch_data = requests.get(stock_endpoint, params=stock_params)
main_data = fetch_data.json()['Time Series (Daily)']
main_data_list = [value for (key,value) in main_data.items()]
yesterday_data = main_data_list[0]
yesterday_data_PRICE = yesterday_data['4. close']

before_yesterday_data =  main_data_list[1]
before_yesterday_data_PRICE = before_yesterday_data['4. close']

price_difference = (float(yesterday_data_PRICE) - float(before_yesterday_data_PRICE))
price_difference_percentage = abs(float(price_difference)/float(yesterday_data_PRICE))

articles = getArticles()
sendMail(articles)