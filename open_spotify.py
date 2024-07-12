import os
import time

# Wi-Fi 연결을 기다리기 위해 잠시 대기
time.sleep(30)

# Chromium 웹 브라우저를 사용하여 Spotify 사이트 열기
os.system("chromium-browser https://open.spotify.com")


# import webbrowser

# # 스포티파이 웹사이트 URL
# spotify_url = "https:/open.spotify.com"

# # 웹 브라우저로 URL 열기
# webbrowser.open(spotify_url)
