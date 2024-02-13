from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas

def fillTheForm(user_name, user_email, hobbies_list, animal_choice):
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)

    driver=webdriver.Chrome(options=chrome_options)
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfBNlrzu_gRa8ujrjzo1GS4OjMWsHs4ah0Q_r1EDkh-miUJnw/viewform?usp=sf_link")

    try:
        fillabe_text = driver.find_elements(By.CLASS_NAME, value="whsOnd")
        hobbies_options=driver.find_elements(By.CLASS_NAME,value="uVccjd")
        radio_button=driver.find_elements(By.CLASS_NAME,value="Od2TWd")

        name_fill = fillabe_text[0]
        email_fill = fillabe_text[1]

        time.sleep(2)

        name_fill.send_keys(user_name)
        email_fill.send_keys(user_email)

        for hobby in hobbies_options:
            if hobby.get_attribute("data-answer-value").lower() in hobbies_list:
                hobby.click()
        for button in radio_button:
            if button.get_attribute("data-value").lower() == animal_choice:
                button.click()

        submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        submit.click()
        time.sleep(1)
        driver.quit()

    except:
        print(str(count)+"Error completing the FROM!!!")
        driver.quit()


def getData():
    data=pandas.read_csv('users.csv')  # All neccessary informations are kept in this .csv file
    my_data=data.to_dict(orient='records')
    for i in range(len(my_data)):
        user_name=my_data[i]['name']
        user_email=my_data[i]['email']
        user_hobbies=my_data[i]['hobbies'].strip().split("-")
        user_animal=my_data[i]['animal']

        fillTheForm(user_name,user_email,user_hobbies,user_animal)

        print(str(count)+". FROM Submitted Successfully!!!")

count=1
getData()

