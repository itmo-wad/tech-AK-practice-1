import os

from flask import render_template, request, redirect, flash, url_for, send_from_directory
from werkzeug.utils import secure_filename

from global_vars import app

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def is_file_allowed(filename):
    return ('.' in filename) and (filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == "GET":
        return render_template('upload.html')
    else:
        if 'fileID' not in request.files:
            flash('No file provided', 'danger')
            return redirect(request.url)

        file = request.files['fileID']

        if file.filename == '':
            flash('No file selected', 'danger')
            return redirect(request.url)

        if not is_file_allowed(file.filename):
            flash('Invalid file extension', 'danger')
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            flash('Successfully saved', 'success')
            return redirect(url_for('showPic', imageName=filename))


@app.route('/upload/<path:imageName>')
def showPic(imageName):
    print(imageName)
    return send_from_directory(app.config['UPLOAD_FOLDER'], imageName)
