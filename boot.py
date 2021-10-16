# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

def do_connect(ssid, password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print("network config: ", sta_if.ifconfig())

# Attempt to connect to WiFi network, my laptop hotspot
do_connect('MDG-Laptop-hotspot', '093Rd+34')

import webrepl
webrepl.start()
