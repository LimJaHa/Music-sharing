import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime
#import serial


cid = '14a5c95dc664471599ccfaf532ba51a6'
secret ='6c9eb1848f4c486b896b75da7f974776'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# 플레이리스트 ID
playlist_id = 'spotify:playlist:4r53elEnWIyPxK0FaMtK7s'


# 특정 사용자의 ID
user_id_1 = '31rpxmyqkd3y6ae3b3n747vn6xk4'  #한솔선배
user_id_2 = '31jpdwjk7olnzg6zm24atyd3mccu'  #나


# 특정 사용자들의 ID 입력받기
user_ids_input = input("Enter user IDs to track, separated by commas: ")
user_ids = [user_id.strip() for user_id in user_ids_input.split(',')]


for i in range(len(user_ids)):
    if user_ids[i] == '1':
        user_ids[i] = user_id_1

    else:
        user_ids[i] = user_id_2

#print(user_ids)


def get_playlist_tracks_with_user(playlist_id):
    # 플레이리스트의 트랙 정보를 가져옴
    playlist = sp.playlist(playlist_id)
    tracks = playlist['tracks']['items']
    # 각 트랙의 이름, 아티스트, 추가한 사용자 ID, 트랙 순서 인덱스를 반환
    return [(index, item['track']['name'], item['track']['artists'][0]['name'], item['added_by']['id'])
            for index, item in enumerate(tracks)]

def get_tracks_by_users(tracks, user_ids):
    # 특정 사용자들이 추가한 트랙 목록을 반환
    user_tracks = [(index, track, artist, added_by) for index, track, artist, added_by in tracks if added_by in user_ids]
    return user_tracks

def print_tracks(tracks):
    for index, track, artist, added_by in tracks:
        print(f"Index: {index}, Track: {track}, Artist: {artist}, Added by: {added_by}")

# 이전 트랙 목록을 저장할 변수 (트랙 인덱스 포함)
previous_tracks = get_playlist_tracks_with_user(playlist_id)
print_tracks(previous_tracks)
print(f"Current tracks added by user {user_ids}:")
user_tracks = get_tracks_by_users(previous_tracks, user_ids)
print_tracks(user_tracks)

# 변경사항을 감지하여 출력하는 루프
#while True:
#    current_tracks = get_playlist_tracks_with_user(playlist_id)
#    if current_tracks != previous_tracks:
#        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#        print(f"Playlist has changed at {current_time}! Current tracks added by users {', '.join(user_ids)}:")
#        user_tracks = get_tracks_by_users(current_tracks, user_ids)
#        print_tracks(user_tracks)
#        previous_tracks = current_tracks
#    time.sleep(60)  # 60초마다 플레이리스트를 확인


while True:
    current_tracks = get_playlist_tracks_with_user(playlist_id)
    if current_tracks != previous_tracks:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"Playlist has changed at {current_time}! Current tracks added by users {', '.join(user_ids)}:")
        user_tracks = get_tracks_by_users(current_tracks, user_ids)
        print_tracks(user_tracks)
        if user_tracks:
            track_uris = [sp.track(track['uri']) for index, track, artist, added_by in user_tracks]
            sp.start_playback(device_id=device_id, uris=track_uris)
        previous_tracks = current_tracks
    # time.sleep(60)  # 60초마다 플레이리스트를 확인