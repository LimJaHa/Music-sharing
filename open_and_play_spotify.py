import time
import os
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# 와이파이가 연결될 때까지 기다리는 함수
def wait_for_wifi():
    while True:
        response = os.system("ping -c 1 google.com")
        if response == 0:
            print("WiFi is connected")
            break
        else:
            print("Waiting for WiFi connection...")
            time.sleep(5)


# 크로미움 웹 브라우저로 스포티파이 웹사이트를 여는 함수
def open_spotify():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://open.spotify.com")

    # 스포티파이 웹사이트가 로드될 때까지 대기
    time.sleep(10)

    # 자동으로 노래 재생 (로그인 필요)
    play_button = browser.find_element_by_xpath("//button[@data-testid='play-button']")
    play_button.click()

if __name__ == "__main__":
    wait_for_wifi()
    open_spotify()
