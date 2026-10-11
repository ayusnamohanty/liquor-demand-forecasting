<<<<<<< HEAD
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
  prediction = None
  if request.method == "POST":
    payload = {
        "Liquor_Retail_Price": float(request.form["price"]),
        "volume_lag_1": float(request.form["lag1"]),
        "volume_roll_mean_3": float(request.form["roll3"]),
        "week_of_year": int(request.form["week"]),
    }
    # Send request to FastAPI running on port 8000
    res = requests.post("http://127.0.0.1:8000/predict", json=payload)
    if res.status_code == 200:
      prediction = res.json()["predicted_bulk_litres"]

  return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
=======
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
  prediction = None
  if request.method == "POST":
    payload = {
        "Liquor_Retail_Price": float(request.form["price"]),
        "volume_lag_1": float(request.form["lag1"]),
        "volume_roll_mean_3": float(request.form["roll3"]),
        "week_of_year": int(request.form["week"]),
    }
    # Send request to FastAPI running on port 8000
    res = requests.post("http://127.0.0.1:8000/predict", json=payload)
    if res.status_code == 200:
      prediction = res.json()["predicted_bulk_litres"]

  return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
>>>>>>> ca4c308f49c5d937a9d74b2555787482bfdc8018
  app.run(port=5000, debug=True)