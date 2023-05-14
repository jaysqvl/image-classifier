#############################################
## Flask Controller Back-end               ##
## 1. Processes the image                  ##
## 2. Loads the pre-trained Pytorch model  ##
## 3. Classifies the image                 ##
## 4. Sends the classification result back ##
##      to the frontend including any      ##
##      visualizations/data                ##
#############################################

import traceback
from flask import Flask, request
from backend import eval, model, preprocess, train

app = Flask(__name__)

@app.route('/preprocess')
def preprocess():
    # stub
    return 0

@app.route('/model')
def modelArc():
    return 0

@app.route('/eval')
def evaluate():
    # stub
    return 0

@app.route('/train')
def train():
    # stub
    return 0

@app.route("/")
def homeRoute():
    return "what are you doing here?"

def main():
    return "Test flask"