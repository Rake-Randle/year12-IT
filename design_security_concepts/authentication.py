from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'jonescaptains'

# ? Sample user data
users = {
    "user1": generate_password_hash("password123")
}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    if username in users and check_password_hash(users[username], password):
        session['user'] = username
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid Credentials'}), 401 
    
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return jsonify({'message': 'Logged out successfully'})

if __name__ == '__main__':
    app.run(debug=True)