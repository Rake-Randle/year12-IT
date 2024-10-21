from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

#! Generate a Hash for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# * Encryption route
@app.route('/encrypt', methods=['POST'])
def encrypt_data():
    data = request.json.get('data')
    encrypted_data = cipher_suite.encrypt(data.encode())
    return jsonify({'encrypted_data': encrypted_data.decode()})

# * Decryption Route
@app.route('/decrypt', methods=['POST'])
def decrypt_data():
    encrypted_data = request.json.get('encrypted_data')
    decrypted_data = cipher_suite.decrypt(encrypted_data.encode())
    return jsonify({'decrypted_data': decrypted_data.decode})

if __name__ == '__main__':
    app.run(debug=True)