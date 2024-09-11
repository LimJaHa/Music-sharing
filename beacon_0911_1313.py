import asyncio
from bleak import BleakScanner

async def scan_beacons():
    def detection_callback(device, advertisement_data):
        if device.name == "MBeacon":
            print(f"Device Name: {device.name}, RSSI: {advertisement_data.rssi}")

    scanner = BleakScanner(detection_callback=detection_callback)

    # 스캔을 시작하고 종료 없이 계속 유지
    await scanner.start()

    # 무한 대기 상태로 유지, 스캔이 계속 진행됨
    while True:
        await asyncio.sleep(1)

async def main():
    await scan_beacons()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
