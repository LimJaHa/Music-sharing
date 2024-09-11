import asyncio
from bleak import BleakScanner

async def scan_beacons():
    devices = []

    def detection_callback(device, advertisement_data):
        if device.name == "MBeacon":
            devices.append((device.name, advertisement_data.rssi))

    # detection_callback을 생성자에 직접 전달
    scanner = BleakScanner(detection_callback=detection_callback)

    # 스캔을 10초간 진행
    await scanner.start()
    await asyncio.sleep(15)
    await scanner.stop()

    for name, rssi in devices:
        print(f"Device: {name}, RSSI: {rssi}")

loop = asyncio.get_event_loop()
loop.run_until_complete(scan_beacons())
