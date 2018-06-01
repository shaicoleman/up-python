from flask import Flask
import sys
import glob

app = Flask(__name__)

@app.route('/')
def hello_world():
  return sys.version
