from weather import app
from flask import render_template, request, jsonify
from .api import *

#===============================================================================# 
# Each Relative Address here defines an API Route that can be called anywhere   #
# (e.g. Browser, Postman, etc.)                                                 #
# The API Address is defined by what is inside @app.route(), not the fn name    #
#===============================================================================#
@app.route("/")
def weather():
  return render_template("weather.html")

@app.route("/get_psi")
def get_psi():
  psi = make_call()
  return jsonify({'psi_twenty_four_hourly': psi})

#===============================================================================# 
# Create a new route here called /magic_psi which returns PSIs of healthy range #
#===============================================================================#
@app.route("/magic_psi", methods=["POST"])
def magic_psi():
	#=============================================#
  # 1. Get the form data from request.data      #
  # 2. Call .decode('utf-8') on the data        #
  # 3. .split() string to get the region string #
  # 4. Set region_psi to arbitrary number       #
  # 5. Return the jsonify-ed object             #
  # ------------------ BONUS ------------------ #
  # 5. Set region_psi value from user input     #
  #=============================================#
	pass