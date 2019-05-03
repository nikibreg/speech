import time
from threading import Timer
from flask import Flask, render_template, flash, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from recognition import recognize

UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__, static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super secret key"



@app.route('/', methods=['GET', 'POST'])
def root():
    return app.send_static_file('index.html')
	

text = "hello my name is green red"
def detectColor(recognizedString):
    for color in ["red", "orange", "blue", "yellow", "green", "purple"]:
        print(recognizedString.find(color))
        if recognizedString.upper().find(color.upper()) != -1:
            return color
        
    return "white"


# def render(filename, recognizedString):
#     return render_template('result.html', recognizedString=recognizedString)

    
    
@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        if os.path.exists("uploads/audio.wav"):
                os.remove("uploads/audio.wav")
        else:
            print("The file does not exist")    
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        # if file.filename == '':
        #     flash('No selected file')
        #     return redirect(request.url)
        recognizedString=""
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(os.path.dirname(__file__), app.config['UPLOAD_FOLDER'], filename))
            recognizedString = recognize()
            print(recognizedString)
        time.sleep(2)

    
            
        return render_template('result.html', recognizedString=recognizedString, hex=detectColor(recognizedString ))


        
        
     
