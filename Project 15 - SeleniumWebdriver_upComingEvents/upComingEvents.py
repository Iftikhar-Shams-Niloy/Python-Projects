from selenium import webdriver
from selenium.webdriver.common.by import By
import fake_useragent
from datetime import datetime

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

def fetchData():
    event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
    event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

    news_times = driver.find_elements(By.CSS_SELECTOR, value=".blog-widget time")
    news_names = driver.find_elements(By.CSS_SELECTOR, value=".blog-widget ul li a")

    time = datetime.now()

    news_info = {}
    event_info = {}

    for i in range(len(event_names)):
        event_info[event_names[i].text] = str(time.year)+"-"+event_times[i].text

    for j in range(len(news_names)):
        news_info[news_names[j].text] = str(time.year)+"-"+news_times[j].text

    return event_info,news_info

def writeData(event_info, news_info):
    with open("eventInfo.txt", "w") as my_file:
        my_file.write("Event,Date\n")
        for key,value in event_info.items():
            my_file.write(key+","+value+"\n")

    with open("newsInfo.txt", "w", encoding="utf-8") as my_file2:
        my_file2.write("News,Date\n")
        for key2,value2 in news_info.items():
            my_file2.write(key2+","+value2+"\n")

try:
    event,news = fetchData()
    writeData(event, news)
    print("DATA SUCCESSFULLY COLLECTED!!!")
except:
    print("DATA COULD NOT BE FETCHED!!!")


driver.quit()
# driver.close()