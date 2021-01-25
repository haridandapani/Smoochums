from flask import Flask
from flask import request
from flask import render_template
from flask import current_app
from flask import send_from_directory
import sqlite3
import random
import string
import os
import smoochfinder

UPLOAD_FOLDER = './uploads'
app = Flask(__name__,static_folder='./static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('home.html', smoochum = "basesmoochum.png")

@app.route('/create', methods=['POST'])
def createsmoochum():
    filename = id_generator() + ".png"
    compfile = 'uploads/' +filename
    smoochfinder.createrandomsmoochum(compfile)
    return render_template('home.html', smoochum = filename)
    

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    print(filename)
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    print(uploads)
    return send_from_directory(directory=uploads, filename=filename)

def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
