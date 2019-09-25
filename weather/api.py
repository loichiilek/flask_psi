import requests
import json
from datetime import datetime
import urllib.parse

#===============================================================================# 
# This function serves to make an API Call to https://data.gov.sg/dataset/psi   #
# and returns a dictionary mapping of PSI in 5 different locations.             #
#===============================================================================#
def make_call():
  #=================================#
  # Input: None                     #
  # Return: Python Dictionary       #
  # Eg:                             #
  # return {                        #
  #   "north" : 50,                 #
  #   "south" : 50,                 #
  #   "east" : 50,                  #
  #   "west" : 50,                  #
  #   "central" : 50                #
  # }                               #
  #=================================#

  return {                        
    "north" : 0,
    "south" : 0,
    "east" : 0,
    "west" : 0,
    "central" : 1
  }  
