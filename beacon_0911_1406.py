import asyncio
from bleak import BleakScanner
import time

async def scan_beacons():
    last_seen_time = None  # 마지막으로 비콘 신호를 감지한 시간을 저장
    home_status_printed = None  # 마지막으로 출력한 상태를 저장
    last_signal_time = time.time()  # 마지막으로 신호를 감지한 시간을 기록

    def detection_callback(device, advertisement_data):
        nonlocal last_seen_time, last_signal_time, home_status_printed  # 변수들을 nonlocal로 선언
        if device.name == "MBeacon":
            rssi = advertisement_data.rssi
            print(f"Device Name: {device.name}, RSSI: {rssi}")
            last_seen_time = time.time()  # 현재 시간을 기록
            last_signal_time = last_seen_time  # 마지막 신호 감지 시간 갱신

            if home_status_printed != "At home":
                print("At home")
                home_status_printed = "At home"

    scanner = BleakScanner(detection_callback=detection_callback)
    await scanner.start()

    while True:
        current_time = time.time()

        # 마지막으로 신호를 감지한 후 5분 이상 지나면 "Not at home" 출력
        if last_seen_time and (current_time - last_seen_time > 5 * 60):
            if home_status_printed != "Not at home":
                print("Not at home")
                home_status_printed = "Not at home"

        # 마지막 신호 감지 후 2초 이상 지나면 "No signal detected" 출력
        if current_time - last_signal_time > 2:
            print("No signal detected")
            last_signal_time = current_time  # 문구가 반복 출력되지 않도록 시간 갱신

        await asyncio.sleep(1)

async def main():
    await scan_beacons()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
