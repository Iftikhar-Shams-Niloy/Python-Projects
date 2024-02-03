from bs4 import BeautifulSoup
import requests
import re

movie_list = []
netflix_movie_list = []
netflix_movie_tomato_rating = []

website_URL = "https://www.empireonline.com/movies/features/best-movies-2/"
website_netflix_URL = "https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/"

webpage = requests.get(website_URL)
webpage_content = webpage.text

netflix_webpage = requests.get(website_netflix_URL)
netflix_content = netflix_webpage.text

my_soup = BeautifulSoup(webpage_content,"html.parser")
my_netflix_soup = BeautifulSoup(netflix_content,"html.parser")

movie_names = my_soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
netflix_names = my_netflix_soup.find_all(name="div", class_="article_movie_title")

def makeList():
    for data in netflix_names:
        fetch = data.find(name="a")
        netflix_movie_list.append(fetch.getText())
        netflix_movie_tomato_rating.append(fetch.get("href"))
    for names in movie_names:
        movie_list.append(names.getText())
    movie_list.reverse()
    print("<<<LISTS MADE SUCCESSFULLY>>>")

def writeFile():
    with open("movie_list.txt", "w") as file1:
        for item in movie_list:
            file1.write(item + "\n")
    with open("netflix_movie_list.txt", "w") as file2:
        for i in range(len(netflix_names)):
            file2.write("NAME: "+netflix_movie_list[i]+"\n")
            file2.write("TOMATO RATING: "+netflix_movie_tomato_rating[i]+"\n")
            file2.write("--------------------------------------------------------------------------------------------\n")
    print("<<<FILES WRITTEN SUCCESSFULLY>>>")

makeList()
writeFile()


