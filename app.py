import os

from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_image', methods=['POST',])
def save_image():
    name = request.form['name']
    archive = request.files['image']

    extension = os.path.splitext(archive.filename)[1]
    f_name = str(name + extension)

    upload_path = app.config['UPLOAD_PATH']

    archive.save(os.path.join(upload_path, f_name))

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True,port=5380)

