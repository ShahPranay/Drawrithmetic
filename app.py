from flask import Flask,redirect, url_for, request,flash
from flask.json import jsonify
from flask.templating import render_template
from markupsafe import escape
from inference import predict_image
from flask import send_from_directory
import base64

app=Flask(__name__)

@app.route("/predict",methods=['POST'])
def predict():
    img_bytes=base64.b64decode(request.form.get("img"))
    val = predict_image(img_bytes)
    return str(val)

# @app.route("/upload")
# def upload():
#     return render_template('upload.html',value=None)

@app.route("/",methods=['GET'])
def draw():
    return render_template('draw.html')
