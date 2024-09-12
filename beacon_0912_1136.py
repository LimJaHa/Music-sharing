import asyncio
import time
import firebase_admin   # pip install firebase-admin
from firebase_admin import credentials, db  # 또는 firestore를 사용할 경우 firestore를 임포트
from bleak import BleakScanner

# Firebase 초기화
cred = credentials.Certificate("./pp-test-2bf23-firebase-adminsdk-q18cp-955c660b63.json")  # 다운로드한 비공개 키 파일 경로
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pp-test-2bf23-default-rtdb.firebaseio.com/'  # Firebase 실시간 데이터베이스 URL 또는 Firestore
})

# Firebase 데이터베이스 참조 (실시간 DB 사용 시)
ref = db.reference('user_status')

async def scan_beacons():
    last_seen_time = None  # 마지막으로 비콘 신호를 감지한 시간을 저장
    home_status_printed = None  # 마지막으로 출력한 상태를 저장
    last_signal_time = time.time()  # 마지막으로 신호를 감지한 시간을 기록

    def detection_callback(device, advertisement_data):
        nonlocal last_seen_time, last_signal_time, home_status_printed
        if device.name == "MBeacon":
            rssi = advertisement_data.rssi
            print(f"Device Name: {device.name}, RSSI: {rssi}")
            last_seen_time = time.time()  # 현재 시간을 기록
            last_signal_time = last_seen_time  # 마지막 신호 감지 시간 갱신

            if home_status_printed != "At home":
                print("At home")
                update_status_to_firebase("At home")  # 상태를 파이어베이스에 업로드
                home_status_printed = "At home"

    scanner = BleakScanner(detection_callback=detection_callback)
    await scanner.start()

    while True:
        current_time = time.time()

        # 마지막으로 신호를 감지한 후 5분 이상 지나면 "Not at home" 출력
        if last_seen_time and (current_time - last_seen_time > 5 * 60):
            if home_status_printed != "Not at home":
                print("Not at home")
                update_status_to_firebase("Not at home")  # 상태를 파이어베이스에 업로드
                home_status_printed = "Not at home"

        # 마지막 신호 감지 후 2초 이상 지나면 "No signal detected" 출력
        if current_time - last_signal_time > 2:
            print("No signal detected")
            last_signal_time = current_time  # 문구가 반복 출력되지 않도록 시간 갱신

        await asyncio.sleep(1)

def update_status_to_firebase(status):
    """파이어베이스에 상태를 업데이트하는 함수"""
    ref.set({
        'status': status,
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # 현재 시간 추가
    })
    print(f"Firebase updated: {status}")

async def main():
    await scan_beacons()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
