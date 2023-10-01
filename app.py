from flask import Flask, request, jsonify
import json
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.json
    username = data.get('username')  
    if username is None:
        return jsonify({'error': 'Username not provided'}), 400
    
   
    cst = pytz.timezone('America/Chicago')
    
    
    timestamp = datetime.now(cst).strftime('%m%d_%I%M%p')
    
    
    filename = f'{username}_{timestamp}.json'
    
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    
    return jsonify({'message': 'Data received and stored successfully!'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
