# ESP32 DHT11 Temperature & Humidity Logger with Flask Backend

## Features
- Collects temperature and humidity data using a DHT11 sensor.  
- Sends data to a Flask server running on a PC/Raspberry Pi.  
- Server stores all sensor readings into a CSV file with timestamps.  
- Handles temporary WiFi/server outages with retries.  
- Auto-start on ESP32 power-up.  

---

## Requirements

### Hardware
- ESP32 board  
- DHT11 sensor  
- Breadboard + jumper wires  
- USB cable for flashing the ESP32  

### Software
- [MicroPython firmware](https://micropython.org/download/esp32/) installed on ESP32  
- [Thonny IDE](https://thonny.org/) or `ampy` to upload code  
- Python 3 with Flask installed on server machine:  
  ```bash
  
  pip install flask


## Auto-start on ESP32

Since the code is saved as main.py on the ESP32, it will automatically run on boot.
This means every time the ESP32 is powered on, it connects to WiFi and starts logging.


