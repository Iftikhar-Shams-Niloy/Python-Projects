# https://appbrewery.github.io/Zillow-Clone/
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

apartment_address_list = []
apartment_info_list = []
apartment_rent_list = []
apartment_link_list = []

def scrapData():
    global apartment_addresses
    global apartment_infos
    global apartment_rents
    global apartment_links

    website_URL = "https://appbrewery.github.io/Zillow-Clone/"
    webpage = requests.get(website_URL)
    webpage_content = webpage.text

    my_soup = BeautifulSoup(webpage_content,"html.parser")

    apartment_addresses = my_soup.select(selector="address")
    apartment_infos = my_soup.select(selector=".StyledPropertyCardHomeDetailsList")
    apartment_rents = my_soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
    apartment_links = my_soup.select('.StyledPropertyCardDataWrapper a', attrs={'href': re.compile("https://")})

def makeLists():
    for adr in apartment_addresses:
        apartment_address_list.append(adr.getText().strip())
    for rent in apartment_rents:
        apartment_rent_list.append(rent.getText())
    for info in apartment_infos:
        processed_info=info.getText().strip().replace("\n"," ")
        if processed_info == "":
            apartment_info_list.append("NO INFO!")
        else:
            apartment_info_list.append(processed_info)
    for link in apartment_links:
        apartment_link_list.append(link["href"])

    print("<---Web Scrapping Successful!--->")

def getForm():
    global my_driver
    form_URL = "https://forms.gle/XvkwYbew98qVVE3f9" # Make a google form like this one and put the link here
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)
    my_driver = webdriver.Chrome(options=chrome_options)
    my_driver.get(form_URL)

def getFormInfo():
    global address_fill
    global info_fill
    global rent_fill
    global link_fill

    fillabe_text = my_driver.find_elements(By.CLASS_NAME, value="whsOnd")
    address_fill = fillabe_text[0]
    info_fill = fillabe_text[1]
    rent_fill = fillabe_text[2]
    link_fill = fillabe_text[3]

def fillForm(address, info, rent, link):
    WebDriverWait(my_driver,10).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')))

    getFormInfo()

    address_fill.clear()
    info_fill.clear()
    rent_fill.clear()
    link_fill.clear()

    address_fill.send_keys(address)
    info_fill.send_keys(info)
    rent_fill.send_keys(rent)
    link_fill.send_keys(link)

    submit = my_driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()

    WebDriverWait(my_driver,10).until(expected_conditions.visibility_of_element_located(
        (By.CLASS_NAME, "c2gzEf")))

    get_back = my_driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    get_back.click()


def passInfo():
    for item in range(len(apartment_address_list)):
        address = apartment_address_list[item]
        info = apartment_info_list[item]
        rent = apartment_rent_list[item]
        link = apartment_link_list[item]
        time.sleep(2)
        fillForm(address,info,rent,link)

    my_driver.quit()
    print("<---Informations Filled Successfully!--->")

############Calling the Methods#############
scrapData()
makeLists()

getForm()
passInfo()