from machine import Pin
import dht
import time
import urequests
import network

# WiFi configuration
SSID = "YOUR_WIFI_NAME"
PASSWORD = "YOUR_WIFI_PASSWORD"

# Flask server address (must include http://)
URL = "http://server_ip_address/data"

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

print("Connecting to WiFi...")
while not wlan.isconnected():
    time.sleep(1)

print("WiFi connected:", wlan.ifconfig())

# Setup DHT11 sensor
dht_pin = Pin(18)
sensor = dht.DHT11(dht_pin)

# Main loop
while True:
    try:
        # Measure temperature and humidity
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temp:", temp, "Hum:", hum)

        # Send data to Flask server
        response = urequests.post(URL, json={"temperature": temp, "humidity": hum})
        response.close()

    except Exception as e:
        print("Error sending data:", e)

    # Wait before next reading (e.g. 60 seconds)
    time.sleep(60)
