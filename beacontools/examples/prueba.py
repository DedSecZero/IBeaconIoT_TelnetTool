import time
from beacontools import BeaconScanner, EddystoneTLMFrame, EddystoneFilter

def callback(bt_addr, rssi, packet, additional_info):
    print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))

# scan for all TLM frames of beacons in the namespace "12345678901234678901"
scanner = BeaconScanner(callback,
    device_filter=EddystoneFilter(namespace="2f234454-cf6d-4a0f-ad2-f4911ba9ffa6"),
    packet_filter=EddystoneTLMFrame
)
scanner.start()

time.sleep(10)
scanner.stop()
