from flask import Flask
from flask import request
from flask import render_template
from flask import current_app
from flask import send_from_directory
from PIL import ImageColor
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

@app.route('/slides', methods=['POST', 'GET'])
def slides():
    if request.method == 'POST':
        num = int(request.form['length'])
        intlen = float(request.form['interval'])     
    else:
        num = 6
        intlen = 50
    smoochums = ""
    for i in range(0, num):
        filename = id_generator() + ".png"
        compfile = 'uploads/' +filename
        smoochfinder.createrandomsmoochum(compfile, True)
        smoochums += filename
        smoochums += ","
    return render_template('slides.html', smoochums = smoochums, smoochum = True, intervalLength = intlen)

@app.route('/create', methods=['POST'])
def createsmoochum():
    filename = id_generator() + ".png"
    compfile = 'uploads/' +filename
    smoochfinder.createrandomsmoochum(compfile, True)
    return render_template('home.html', smoochum = filename)
    
@app.route('/collage', methods=['POST'])
def createsmoochumcollage():
    filename = id_generator() + ".png"
    compfile = 'uploads/' +filename
    width = int(request.form['width'])
    height = int(request.form['height'])
    smoochfinder.collage(compfile, width, height)
    return render_template('home.html', smoochum = filename)

@app.route('/custom', methods=['POST'])
def createcustomsmoochum():
    try:
        filename = id_generator() + ".png"
        compfile = 'uploads/' +filename
        hair = ImageColor.getcolor(request.form['hair'], "RGBA")
        eyes = ImageColor.getcolor(request.form['eyes'], "RGBA")
        bg = ImageColor.getcolor(request.form['bg'], "RGBA")
        lips = ImageColor.getcolor(request.form['lips'], "RGBA")
        iris = ImageColor.getcolor(request.form['iris'], "RGBA")
        skin = ImageColor.getcolor(request.form['skin'], "RGBA")
        shadow = ImageColor.getcolor(request.form['shadow'], "RGBA")
        eye_shadow = ImageColor.getcolor(request.form['eye_shadow'], "RGBA")
        eye_whites = ImageColor.getcolor(request.form['eye_whites'], "RGBA")
        other = ImageColor.getcolor(request.form['other'], "RGBA")
        smoochfinder.smoochummaker(hair, eyes, bg, lips, iris, skin, shadow, eye_shadow, eye_whites, other, compfile, True)
    except Exception as e:
        print(e)
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
