import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# 환경 변수 설정
CLIENT_ID = '14a5c95dc664471599ccfaf532ba51a6'
CLIENT_SECRET = '6c9eb1848f4c486b896b75da7f974776'
REDIRECT_URI = 'http://localhost:8888/callback'


scope = "user-library-read user-library-modify user-read-playback-state user-modify-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,scope=scope, cache_path='/path/to/.cache'))


# 스포티파이 API 인증
#scope = "user-modify-playback-state user-read-playback-state"
#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI,scope=scope))

# 트랙 URI를 입력받아 재생하는 함수
def play_track(uri):
    # 현재 재생 장치를 가져옴
    devices = sp.devices()
    if not devices['devices']:
        print("No devices found. Please open Spotify on your device.")
        return

    # 첫 번째 장치에서 재생
    device_id = devices['devices'][0]['id']
    print("device id is..", device_id)
    sp.start_playback(device_id=device_id, uris=[uri])
    print(f"Playing track: {uri}")

# 재생하고자 하는 트랙 URI
track_uri = input("Enter the Spotify track URI: ")

# 트랙 재생
play_track(track_uri)

#예뻤어 링크
# https://open.spotify.com/track/3HAkoNmThZhyFejhpRXXYI?si=5bd17a0f636b4015