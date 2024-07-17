import spotipy
from spotipy.oauth2 import SpotifyOAuth

# 환경 변수 설정
CLIENT_ID = '14a5c95dc664471599ccfaf532ba51a6'
CLIENT_SECRET = '6c9eb1848f4c486b896b75da7f974776'
REDIRECT_URI = 'http://localhost:8888/callback'

# 인증 스코프 설정 (볼륨 조절을 위해 user-modify-playback-state 스코프 필요)
scope = 'user-modify-playback-state user-read-playback-state'

# Spotify OAuth 인증 객체 생성
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope))

# 현재 활성화된 장치 가져오기
devices = sp.devices()
if devices['devices']:
    active_device_id = devices['devices'][0]['id']
    print(f"Active device ID: {active_device_id}")

    # 볼륨 조절 (예: 50%로 설정)
    volume_percent = 50
    sp.volume(volume_percent, device_id=active_device_id)
    print(f"Volume set to {volume_percent}%")
else:
    print("No active device found")
