from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# 사용자 정보 설정
spotify_email = 'limjaha@unist.ac.kr'
spotify_password = 'L!Mj@h@7535'

# 크롬 드라이버 경로 설정
chrome_driver_path = '/path/to/chromedriver'

# 크롬 옵션 설정
chrome_options = webdriver.ChromeOptions()

# 브라우저 꺼짐 방지 옵션
chrome_options.add_experimental_option("detach", True)

chrome_options.binary_location = chrome_driver_path

# 브라우저 열기
driver = webdriver.Chrome(options=chrome_options)

# 스포티파이 로그인 페이지 열기
driver.get('https://accounts.spotify.com/ko/login?continue=https%3A%2F%2Fopen.spotify.com%2F')

try:
    # 이메일 입력 필드가 로드될 때까지 기다리기
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'login-username'))
    )
    # 이메일 입력
    email_field.send_keys(spotify_email)

    # 비밀번호 입력 필드가 로드될 때까지 기다리기
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'login-password'))
    )
    # 비밀번호 입력
    password_field.send_keys(spotify_password)

    # 로그인 버튼이 로드될 때까지 기다리기
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'login-button'))
    )
    # 로그인 버튼 클릭
    login_button.click()

    # 로그인 후 페이지가 로드될 때까지 기다리기
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="root"]'))
    )

    print("로그인 성공!")

    driver.get('https://open.spotify.com')

except Exception as e:
    print(f"로그인 중 오류 발생: {e}")

finally:
    # 작업이 끝난 후 브라우저 닫기 (필요시 주석 처리)
    time.sleep(10)  # 로그인 후 몇 초 동안 대기

