from flask import Flask, request, jsonify

app = Flask(__name__)

# ! In-memory storage for demonstration purposes
users = {}

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    email = request.json.get('email')
    
    # * Data minimisation - only store essesntial information
    users[username] = {'email': email}
    return jsonify({'message': 'User registered successfully'})

@app.route('/delete_user', methods=['POST'])
def delete_user():
    username = request.json.get('username')
    
    if username in users:
        del users[username]
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)