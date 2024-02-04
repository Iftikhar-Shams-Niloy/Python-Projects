from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Enter date (format: YYYY-MM-DD): ")
song_names = []
artist_names = []
song_URIs = []

website_URL = (f"https://www.billboard.com/charts/hot-100/{date}/")

website = requests.get(website_URL)
website_content = website.text

my_soup = BeautifulSoup(website_content,"html.parser")

song_info = my_soup.select("li ul li h3")
artist_info = my_soup.select("div ul li ul li span")

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
    year = date.split("-")[0]
    with open("my_info.txt","r") as info:
        client_id = str(info.readline().strip())
        client_secret = str(info.readline().strip())
    my_spotipy = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= client_id,
                                                    client_secret= client_secret,
                                                    redirect_uri="http://example.com",
                                                    scope="playlist-read-private, " \
                                                        "user-read-currently-playing, " \
                                                        "user-read-currently-playing, " \
                                                        "user-follow-read, playlist-modify-private",
                                                    show_dialog=True,
                                                    cache_path="token.txt"))
    user_id = my_spotipy.current_user()["id"]
    for song,artist in zip(song_names,artist_names):
        result = my_spotipy.search(q=f"track:{song} artist:{artist}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_URIs.append(uri)
            print(f"<<<{song} ADDED SUCCESSFULLY.>>>")
        except IndexError:
            print(f"<<<{song} DOES NOT EXIST!!!>>>")

    playlist = my_spotipy.user_playlist_create(user=user_id,name=f"{date} Billboard 100",public=False,)
    my_spotipy.playlist_add_items(playlist_id=playlist["id"],items=song_URIs)
    print(f"New playlist '{date} Billboard 100' successfully created on Spotify!")


makeLists()
makeSpotifyPlaylist()