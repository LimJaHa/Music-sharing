import time
import webbrowser


def open_spotify():
    url = "https://www.spotify.com"
    webbrowser.get("chromium-browser").open(url)
    time.sleep(10)  # 페이지 로딩 시간 대기

def play_music():
    # 스포티파이에서 재생 버튼을 클릭하기 위한 selenium 사용
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")

    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://open.spotify.com")

    # 재생 버튼 찾기
    time.sleep(5)  # 페이지 로딩 시간 대기
    play_button = driver.find_element(By.CLASS_NAME, 'control-button')
    play_button.click()


open_spotify()
play_music()