"""
Notes from the course:
Confidentiality - Ensures that sensitive information remains priate by encrypting data 
Integrity - hashing verifies that data has not been altered through data communications
Authentication - verify the identities of users and devices
Non-repudiation - digital signitures, crupto evidence, provide proof of origin and integrity of data
"""
from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

# ! Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/encrypt', methods=['POST'])
def encrypt_data():
    data = request.json.get('data')
    encrypted_data = cipher_suite.encrypt(data.encode())
    return jsonify({'encrypted_data': encrypted_data.decode()})

@app.route('/decrypt', methods=['POST'])
def decrypt_data():
    encrypted_data = request.json.get('encrypted_data')
    decrypted_data = cipher_suite.decrypt(encrypted_data.encode())
    return jsonify({'decrypted_data': decrypted_data.decode()})

if __name__== '__main__':
    app.run(debug=True)