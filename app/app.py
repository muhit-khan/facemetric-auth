import os
import secrets
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from deepface import DeepFace
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


def generate_random_folder():
    """Generates a random directory name for secure file uploads."""
    return secrets.token_hex(8)

app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def compare_photos(reference_image_path, live_image_path):
    try:
        result = DeepFace.verify(img1_path=reference_image_path, img2_path=live_image_path)
        return result['verified']
    except Exception as e:  
        print(f"Error during face comparison: {e}")
        return "Comparison Failed"


@app.route('/compare', methods=['POST'])
def compare():
    if 'reference_image' not in request.files or 'live_image' not in request.files:
        return jsonify({'error': 'Missing reference or live image files'}), 400

    reference_image = request.files['reference_image']
    live_image = request.files['live_image']

    if reference_image.filename == '' or live_image.filename == '':
        return jsonify({'error': 'Empty file names'}), 400

    if not allowed_file(reference_image.filename) or not allowed_file(live_image.filename):
        return jsonify({'error': 'Invalid file format'}), 400

    
    upload_folder = os.path.join(app.config['UPLOAD_FOLDER'], generate_random_folder())
    os.makedirs(upload_folder)  

    try:
        filename1 = secure_filename(reference_image.filename)
        filename2 = secure_filename(live_image.filename)
        reference_image_path = os.path.join(upload_folder, filename1)
        live_image_path = os.path.join(upload_folder, filename2)

        reference_image.save(reference_image_path)
        live_image.save(live_image_path)

        result = compare_photos(reference_image_path, live_image_path)

        
        os.remove(reference_image_path)
        os.remove(live_image_path)
        os.rmdir(upload_folder)  

        return jsonify({'identical': result})
    except Exception as e:
        print(f"Error during file processing: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0', port=5000)
