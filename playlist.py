import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

cid = '14a5c95dc664471599ccfaf532ba51a6'
secret ='6c9eb1848f4c486b896b75da7f974776'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


#result = sp.search("coldplay", limit=1, type='artist')
#pprint.pprint(result)


pl_id = 'spotify:playlist:4r53elEnWIyPxK0FaMtK7s'
offset = 0

while True:
    response = sp.playlist_items(pl_id,
                                 offset=offset,
                                 fields='items.track.id,total',
                                 additional_types=['track'])



    if len(response['items']) == 0:
        break

    pprint(response['items'])
    offset = offset + len(response['items'])
    print(offset, "/", response['total'])





