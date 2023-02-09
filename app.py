from flask import Flask
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/') #localhost:5000/shivan
def home():
    return "this is our first docker file"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)