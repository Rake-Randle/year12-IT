from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = {
    "admin": {"password": generate_password_hash("adminpass"), "role": "admin"},
    "user": {"password": generate_password_hash("userpass"), "role": "user"}
}

@app.route('/login', methods=['POST'])
def loing():
    username = request.json.get('username')
    password = request.json.get('password')
    
    if username in users and check_password_hash(users[username]['password'], password):
        session['user'] = username
        session['role'] = users[username]['role']
        return jsonify({'message': 'Login successful'})
    else: 
        return jsonify({'message': 'Invalid credentials'}), 401
    
@app.route('/admin_resource', methods=['GET'])
def admin_resource():
    if 'user' in session and session['role'] == 'admin':
        return jsonify({'message': 'Admin resource accessed'})
    else:
        return jsonify({'message': 'Access denied'}), 403
    
if __name__ == '__main__':
    app.run(debug=True)        