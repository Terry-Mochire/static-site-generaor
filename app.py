#!/usr/bin/env python3
import os

from flask import Flask, request, flash, redirect, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return "No files to be uploaded"
        for file in request.files.getlist('file'):
            if file.filename == '':
                return "Files have no name"
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return "File uploaded successfully"


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == '__main__':
    app.run(debug=True)
