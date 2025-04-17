# main.py
import network
import time
import urequests
import ntptime
from machine import Pin, reset
import secrets

# Your location
LAT = 34.0522  # Example: Los Angeles
LON = -118.2437

led = Pin("LED", Pin.OUT)

def blink(times, speed=0.3):
    for _ in range(times):
        led.value(1)
        time.sleep(speed)
        led.value(0)
        time.sleep(speed)
    led.value(0)

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets.ssid, secrets.password)
    for _ in range(30):
        if wlan.isconnected():
            return True
        time.sleep(0.5)
    return False

def sync_time():
    try:
        ntptime.settime()
        return True
    except:
        return False

def get_iss_passes(lat, lon):
    url = f"http://api.open-notify.org/iss-pass.json?lat={lat}&lon={lon}"
    try:
        res = urequests.get(url)
        data = res.json()
        res.close()
        return data['response']
    except:
        return []

def main():
    if not connect():
        blink(2)
        return
    if not sync_time():
        blink(3)
        return

    # Everything good – light solid ON
    led.value(1)

    iss_passes = get_iss_passes(LAT, LON)
    next_update = time.time() + 7200  # update every 2 hours

    while True:
        now = time.time()

        if now >= next_update:
            iss_passes = get_iss_passes(LAT, LON)
            next_update = now + 7200

        in_pass = False
        for p in iss_passes:
            risetime = p['risetime']
            duration = p['duration']
            warn_time = risetime - 300  # 5 minutes before

            if warn_time <= now < risetime:
                # ISS approaching – slow blink
                led.value(1)
                time.sleep(0.5)
                led.value(0)
                time.sleep(0.5)
                in_pass = True
                break
            elif risetime <= now <= (risetime + duration):
                # ISS overhead – fast blink
                led.value(1)
                time.sleep(0.15)
                led.value(0)
                time.sleep(0.15)
                in_pass = True
                break

        if not in_pass:
            led.value(1)
            time.sleep(5)

try:
    main()
except:
    led.value(0)
    time.sleep(10)
    reset()
