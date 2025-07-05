from bs4 import BeautifulSoup
import requests
import re

webpage = requests.get("https://www.shopify.com/blog/motivational-quotes")
webpage_content = webpage.text

my_soup = BeautifulSoup(webpage_content,'html.parser')

find_quotes = my_soup.find_all(name='li')
quotes = []

def fetchInfo():
    for items in find_quotes:
        try:
            if items.getText()[0] == "“":
                quotes.append(items.getText())
        except:
            continue
    print("<<<INFORMATION FETCHED SUCCESSFULLY>>>")

def writeInfo():
    with open("quotes.txt","w") as my_file:
        for k in range(len(quotes)):
            # print(str(k+1)+". "+str(quotes[k])+"\n")
            try:
                my_file.write(str(quotes[k])+"\n")
            except:
                print("<<<<<<<>>>>>>>>")
                print("<<< ERROR!!! >>>")
                print("<<<<<<<>>>>>>>>")
                continue
    print("<<<INFORMATION WRITTEN SUCCESSFULLY>>>")

fetchInfo()
writeInfo()
