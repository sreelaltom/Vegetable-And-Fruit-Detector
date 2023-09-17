from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Set the directory where uploaded images will be stored
# UPLOAD_FOLDER = r"E:\GIT\vegetable\static\Images"
upload_folder = os.path.join('static', 'uploads')
app.config['UPLOAD'] = upload_folder

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # # Check if the post request has a file part
        # if 'file' not in request.files:
        #     return redirect(request.url)

        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)

        # # If the user does not select a file, the browser should also submit an empty file
        # if file.filename == '':
        #     return redirect(request.url)

        # if file:
        #     # Save the uploaded image to the UPLOAD_FOLDER
        #     image_path = UPLOAD_FOLDER+f'\{file.filename}'
        #     file.save(image_path)

            # Render the upload.html template with the image_path
        return render_template('upload.html', image_path=img)

    # Render the upload.html template initially
    return render_template('upload.html', image_path=None)


