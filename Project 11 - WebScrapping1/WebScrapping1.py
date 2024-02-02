from bs4 import BeautifulSoup
import requests
import re

webpage = requests.get("https://news.ycombinator.com/news")
webpage_content = webpage.text

my_soup = BeautifulSoup(webpage_content,'html.parser')

find_articles = my_soup.find_all('a',attrs={'href': re.compile("https://")})
points_info = my_soup.find_all(name='span', class_='score')
article_titles = []
article_links = []
article_points = []
def fetchInfo():
    for items in find_articles:
        article_titles.append(items.getText())
        article_links.append(items.get('href'))
        print(items.getText())
        print(items.get('href'))
        print("##########################################################")
    for points in points_info:
        fetch = int((points.getText()).split()[0])
        article_points.append(fetch)
    print("<<<INFORMATION FETCHED SUCCESSFULLY>>>")

def SelectionSort(points,titles,links):
    size = len(points)
    for i in range(size):
        min = i
        for j in range(i+1,size):
            if points[j] < points[min]:
                min = j
        points[i],points[min] = points[min],points[i]
        titles[i],titles[min] = titles[min],titles[i]
        links[i], links[min] = links[min], links[i]
    points.reverse()
    titles.reverse()
    links.reverse()
    print("<<<SORTING DONE SUCCESSFULLY>>>")

def writeInfo():
    with open("news_info.txt","w") as my_file:
        for k in range(len(article_points)):
            my_file.write("Title: "+article_titles[k]+"\n")
            my_file.write("Link: "+article_links[k]+"\n")
            my_file.write("Points: "+str(article_points[k])+"\n")
            my_file.write("------------------------------------------------------------------------------------------\n")
    print("<<<INFORMATION WRITTEN SUCCESSFULLY>>>")

fetchInfo()
SelectionSort(article_points,article_titles,article_links)
writeInfo()

# print(len(article_links))
# print(len(article_titles))
# print(len(article_points))

# Scrapping can be illegal in many websites.
# Use "/robots.txt" at the end of any website to see whether it is allowed to scrap or not.
