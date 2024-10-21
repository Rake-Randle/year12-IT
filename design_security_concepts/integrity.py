import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hash', methods=['POST'])
def hash_data():
    data = request.json.get('data')
    data_hash = hashlib.sha256(data.encode()).hexdigest()
    return jsonify({'hash': data_hash})

@app.route('/verify', methods=['POST'])
def verify_data():
    data = request.json.get('data')
    data_hash = request.json.get('hash')
    new_hash = hashlib.sha256(data.encode()).hexdigest()
    if new_hash == data_hash:
        return jsonify({'message': 'Data is intact'})
    else:
        return jsonify({'message': 'Data has been altered'})

if __name__ == '__main__':
    app.run(debug=True)
    
        