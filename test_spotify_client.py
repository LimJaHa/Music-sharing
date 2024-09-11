import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="14a5c95dc664471599ccfaf532ba51a6",
                                               client_secret="6c9eb1848f4c486b896b75da7f974776",
                                               redirect_uri="spotify:playlist:4r53elEnWIyPxK0FaMtK7s",
                                               scope="user-modify-playback-state user-read-playback-state"))
