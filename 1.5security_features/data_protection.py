from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet

app = Flask(__name__)

# ! generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/store_data', methods=['POST'])
def store_data():
    data = request.json.get('data')
    encrypted_data = cipher_suite.encrypt(data.encode())
    # * Store encrypted data in a secure database (example assumes data is stored)
    return jsonify({'message': 'Data encrypted and store securely'})

@app.route('/retrieve_data', methods=['POST'])
def retrieve_data():
    encrypted_data = request.json.get('encrypted_data')
    decrypted_data = cipher_suite.decrypt(encrypted_data.encode())
    return jsonify({'data': decrypted_data.decode()})

if __name__ == '__main__':
    app.run(debug=True)    