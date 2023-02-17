#!/usr/bin/env python3
import os

from flask import Flask, request, redirect, render_template, abort
from jinja2 import FileSystemLoader, ChoiceLoader
from werkzeug.utils import secure_filename

import generator

app = Flask(__name__)
template_dirs = ['output/templates/', 'templates/']
loaders = [FileSystemLoader(d) for d in template_dirs]
loader = ChoiceLoader(loaders)
app.jinja_loader = loader
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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

        return redirect('/load')


@app.route('/load', methods=['GET'])
def load():
    if request.method == 'GET':
        generator.generate_site('uploads/', 'output/')
        return redirect('/index.html')


@app.route('/index.html', methods=['GET'])
def index_html():
    if request.method == 'GET':
        try:
            return render_template('index.html')
        except:
            abort(404)


@app.route('/about.html', methods=['GET'])
def about_html():
    if request.method == 'GET':
        try:
            return render_template('about.html')
        except:
            abort(404)


@app.route('/contact.html', methods=['GET'])
def contact_html():
    if request.method == 'GET':
        try:
            return render_template('contact.html')
        except:
            abort(404)


@app.route('/articles.html', methods=['GET'])
def articles_html():
    if request.method == 'GET':
        try:
            return render_template('articles.html')
        except:
            abort(404)


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
