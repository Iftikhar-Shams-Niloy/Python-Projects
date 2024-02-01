from bs4 import BeautifulSoup
import requests
import re

webpage = requests.get("https://news.ycombinator.com/news")
webpage_content = webpage.text

my_soup = BeautifulSoup(webpage_content,'html.parser')

find_articles = my_soup.find_all('a',attrs={'href': re.compile("https://")})
article_titles = []
article_links = []

for items in find_articles:
    article_titles.append(items.getText())
    article_links.append(items.get('href'))
    print(items.getText())
    print(items.get('href'))
    print("#######################################")