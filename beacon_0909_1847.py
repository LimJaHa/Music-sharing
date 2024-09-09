import asyncio
from bleak import BleakScanner
from collections import defaultdict

async def scan_beacons():
    devices = defaultdict(lambda: {'count': 0, 'rssi_sum': 0})

    def detection_callback(device, advertisement_data):
        if device.name == "MBeacon":
            if device.name not in devices:
                devices[device.name] = {'count': 0, 'rssi_sum': 0}
            devices[device.name]['count'] += 1
            devices[device.name]['rssi_sum'] += advertisement_data.rssi

    # detection_callback을 생성자에 직접 전달
    scanner = BleakScanner(detection_callback=detection_callback)

    # 스캔을 20초간 진행
    await scanner.start()
    await asyncio.sleep(20)
    await scanner.stop()

    # RSSI 값의 평균을 계산하여 출력
    for name, data in devices.items():
        average_rssi = data['rssi_sum'] / data['count']
        print(f"Device Name: {name}, Average RSSI: {average_rssi:.2f}")

loop = asyncio.get_event_loop()
loop.run_until_complete(scan_beacons())
