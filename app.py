from flask import Flask, render_template, flash, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from main import main

UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__, static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super secret key"


@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(os.path.dirname(__file__), app.config['UPLOAD_FOLDER'], filename))
            print(main())


        
    # return '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form method=post enctype=multipart/form-data>
    #   <input type=file name=file>
    #   <input type=submit value=Upload>
    # </form>
    # '''
    return app.send_static_file('index.html')
	
