from flask import Flask, request
import csv
import time

app = Flask(__name__)

@app.route("/data", methods=["POST"])
def data():
    content = request.get_json()
    temp = content["temperature"]
    hum = content["humidity"]
    ts = time.strftime("%Y-%m-%d %H:%M:%S")

    # Save data to CSV file
    with open("data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([ts, temp, hum])

    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
