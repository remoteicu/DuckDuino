from flask import Flask, request, jsonify, send_from_directory
import os
import json
import base64
from datetime import datetime
import pytz

app = Flask(__name__, static_url_path='/uploads', static_folder='uploads')

BASE_UPLOAD_FOLDER = 'uploads'
app.config['BASE_UPLOAD_FOLDER'] = BASE_UPLOAD_FOLDER

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['BASE_UPLOAD_FOLDER'], filename)

@app.route('/api', methods=['POST'])
def api():
    if request.content_type != 'application/json':
        return jsonify({'error': 'Invalid Content-Type, expected application/json'}), 415

    data = request.get_json()
    if not data or 'image' not in data or 'username' not in data or 'computername' not in data:
        return jsonify({'error': 'No image, username, or computername in the request'}), 400

    image_base64 = data['image']
    username = data['username']
    computername = data['computername']

    cst = pytz.timezone('America/Chicago')
    timestamp = datetime.now(cst).strftime('%m%d_%I%M%p')

    folder_name = f'{username}_{timestamp}'
    upload_folder = os.path.join(app.config['BASE_UPLOAD_FOLDER'], folder_name)
    os.makedirs(app.config['BASE_UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(upload_folder, exist_ok=True)

    image_data = base64.b64decode(image_base64)
    image_filename = f'{username}_{timestamp}.jpeg'
    image_filepath = os.path.join(upload_folder, image_filename)
    with open(image_filepath, 'wb') as image_file:
        image_file.write(image_data)

    json_data = {'username': username, 'computername': computername}
    data_filename = f'{username}_{timestamp}.json'
    with open(os.path.join(upload_folder, data_filename), 'w') as data_file:
        json.dump(json_data, data_file, indent=4)

    image_url = f'{request.url_root}uploads/{folder_name}/{image_filename}'
    return jsonify({'message': 'Data and image received and stored successfully!', 'image_url': image_url}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443)

