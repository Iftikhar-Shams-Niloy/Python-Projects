from bs4 import BeautifulSoup
import requests
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Enter date (format: YYYY-MM-DD): ")

website_URL = (f"https://www.billboard.com/charts/hot-100/{date}/")

website = requests.get(website_URL)
website_content = website.text

my_soup = BeautifulSoup(website_content,"html.parser")

song_info = my_soup.select("li ul li h3")
artist_info = my_soup.select("div ul li ul li span")

song_names = []
artist_names = []

def makeLists():
    print("=================================================================")
    print("============================SONG NAMES===========================")
    print("=================================================================")
    for names in song_info:
        info = names.getText().strip()
        song_names.append(info)
        print(info)
    print("=================================================================")
    print("===========================ARTIST NAMES==========================")
    print("=================================================================")
    for i in range(len(artist_info)):
        if i%7 == 0:
            info = artist_info[i].getText().strip()
            artist_names.append(info)
            print(info)

def makeSpotifyPlaylist():
    my_spotipy = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="9fc6337b49e34ec2abc3f1af117ff3d7",
                                                   client_secret="329bee95778a43ae9072393ae3c213fc",
                                                   redirect_uri="http://example.com",
                                                   scope="user-library-read"))
    results = my_spotipy.current_user_saved_tracks()
    print(results)

makeLists()
makeSpotifyPlaylist()