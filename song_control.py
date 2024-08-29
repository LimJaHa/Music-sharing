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
    
else:
    print("No active device found")

# def previous_track():
#     sp.previous_track(device_id=active_device_id)

# previous_track()

def toggle_playback():
    playback = sp.current_playback()
    
    if playback is not None and playback['is_playing']:
        # 음악이 재생 중인 경우
        sp.pause_playback(device_id=playback['device']['id'])
        print("음악을 일시정지했습니다.")
    else:
        # 음악이 일시정지 상태인 경우
        sp.start_playback(device_id=playback['device']['id'])
        print("음악을 재생했습니다.")

toggle_playback()
