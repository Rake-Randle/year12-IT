from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# ? Sample user data with roles
users = {
    "admin": {"password": "password123", "role": "admin"},
    "user1": {"password": "user1", "role": "user"}
}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    if username in users and users[username]["password"] == password:
        session['user'] = username
        session['role'] = users[username]['role']
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
    
@app.route('/admin', methods=['GET'])
def admin_page():
    if 'user' in session and session['role'] == 'admin':
        return jsonify({'message': 'Welcome to the admin page'})
    else: 
        return jsonify({'message': 'Access Denied'}), 403
    
if __name__ == '__main__':
    app.run(debug=True)