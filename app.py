from flask import Flask,redirect, url_for, request,flash
from flask.templating import render_template
from markupsafe import escape
from inference import predict

Allowed_extensions=set(['png', 'jpg', 'jpeg'])
Upload_folder="/images/"

app=Flask(__name__)
app.config['UPLOAD_FOLDER']=Upload_folder
app.secret_key='secretkey123123123'

def allowed_filename(filename):
    return '.' in filename and filename.split('.',1)[1].lower() in Allowed_extensions

@app.route("/")
def homepage():
    return f"helo. two buttons one for uploading file one for drawing"

@app.route("/predict",methods=['GET','POST'])
def helloworld():
    if request.method == 'POST':
        if "img" not in request.files:
            flash("no file part")
        f=request.files["img"]
        if f and allowed_filename(f.filename):
            img_bytes=f.read()
            val = predict(img_bytes)
            return render_template('upload.html',value=val)
        else:
            flash("Invalid file")
    return render_template('upload.html',value=None)



@app.route("/draw")
def draw():
    return "<p>this is where i'll implement drawing logic</p>"
