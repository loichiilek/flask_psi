from weather import app
from flask import render_template, request, jsonify
from .api import *

@app.route("/")
def weather():
  return render_template("weather.html")

@app.route("/get_psi")
def get_psi():
  psi = make_call()
  return jsonify({'psi_twenty_four_hourly': psi})