from flask import Flask, request, render_template_string
import csv
import time

app = Flask(__name__)


@app.route("/data", methods=["POST"])
def data():
    content = request.get_json()
    temp = content["temperature"]
    hum = content["humidity"]
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    filename = time.strftime("%Y-%m-%d") + ".csv"

    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([ts, temp, hum])

    return {"status": "ok"}, 200


@app.route("/today")
def today():
    filename = time.strftime("%Y-%m-%d") + ".csv"
    try:
        with open(filename, "r") as f:
            rows = list(csv.reader(f))
    except FileNotFoundError:
        return "<h2>No data for today</h2>", 404

    if not rows:
        return "<h2>No readings yet</h2>", 404

    last = rows[-1]
    temp = last[-2]
    hum = last[-1]

    html = f"""
    <!doctype html>
    <html>
    <head>
      <meta charset="utf-8">
      <title>Sensor Bubble</title>
      <style>
        body {{
          background: #111;
          display: flex;
          align-items: center;
          justify-content: center;
          height: 100vh;
          margin: 0;
        }}
        .bubble {{
          width: 220px;
          height: 220px;
          border-radius: 50%;
          background: radial-gradient(circle at 30% 30%, #4fc3f7, #0288d1);
          display: flex;
          align-items: center;
          justify-content: center;
          color: white;
          font-family: sans-serif;
          text-align: center;
          box-shadow: 0 0 40px rgba(0,150,255,0.7);
          animation: float 6s ease-in-out infinite;
        }}
        @keyframes float {{
          0% {{ transform: translateY(0px); }}
          50% {{ transform: translateY(-25px); }}
          100% {{ transform: translateY(0px); }}
        }}
        .value {{
          font-size: 2em;
          font-weight: bold;
        }}
      </style>
    </head>
    <body>
      <div class="bubble">
        <div>
          <div>🌡️ {temp} °C</div>
          <div class="value">💧 {hum}%</div>
        </div>
      </div>
    </body>
    </html>
    """
    return render_template_string(html)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=*port number*, debug=False)
