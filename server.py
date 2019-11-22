import os     
abs_app_dir_path = os.path.dirname(os.path.realpath(__file__))
print(abs_app_dir_path)

abs_views_path = os.path.join(abs_app_dir_path, 'views')
import bottle
print(bottle.TEMPLATE_PATH)
bottle.TEMPLATE_PATH.insert(0, abs_views_path )

from horoscope import generate_prophecies
from bottle import route, run, view, static_file
from datetime import datetime as dt

@route("/")
@view("predictions")
def index():
  now = dt.now()

  

  return {
    "special_date": False,
    "predictions": generate_prophecies(),
    "date": f"{now.year}-{now.month}-{now.day}",
    # "predictions": [
    #  ["Раз", "Два", "Три"]
    # ]
  }

@route("/api/test")
def api_test():
    return {"test_passed": True}

@route("/api/forecast")
def forecast():
  return {
  "prophecies": 
  generate_prophecies(total_num=6, num_sentences=2)
  }

@route("/helpers.js")
def helper_js():
  return static_file("helpers.js", root="static")

@route("/styles.css")
def styles_css():
  return static_file("styles.css", root="static")

run(
  host="localhost",
  port=8080,
  autoreload=True,
  debug=True
)

