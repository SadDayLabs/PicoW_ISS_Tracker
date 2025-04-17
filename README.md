# Pico ISS Tracker

A tiny, standalone, Wi-Fi-connected ISS LED notifier using the Raspberry Pi Pico W and MicroPython.

## What It Does

- Connects to Wi-Fi
- Uses [Open Notify API](http://open-notify.org) to fetch flyover times for your location
- Controls the onboard LED to let you know when the ISS is about to fly by

## LED Behavior

| System State         | LED Behavior         |
|----------------------|----------------------|
| Booting / Idle       | Off                  |
| Running OK           | Solid ON             |
| ISS 5 min away       | Blink slowly (1/sec) |
| ISS overhead         | Blink fast (3/sec)   |
| Wi-Fi error          | Blink 2× slowly, then OFF |
| Time sync error      | Blink 3× slowly, then OFF |
| Script crash         | LED OFF              |

## Setup Instructions

1. Flash [MicroPython](https://micropython.org/download/rp2-pico-w/) to your Pico W using [Thonny](https://thonny.org)
2. Upload `main.py` and a renamed copy of `secrets.py.example` → `secrets.py`
3. Edit `LAT` and `LON` in `main.py` to match your location
4. Plug in power — the LED will handle the rest!

## Files

- `main.py`: Main script that handles Wi-Fi, time sync, and ISS tracking *Edit LAT and LON
- `secrets.py.example`: Template for your Wi-Fi credentials
- `LICENSE`: MIT License

## Thanks & Credits

- MASSIVE THANK YOU TO OPEN NOTIFY. Your API is rad.
- **[Open Notify](http://open-notify.org)** – for the free, public ISS tracking API.
- Built by Sad Day Labs. Use it, remix it, and share it freely. I don't give a hoot. ❤️

## 🌐 License

MIT — free to use, modify, and distribute. Attribution appreciated but not required.

~Sad Day Labs
