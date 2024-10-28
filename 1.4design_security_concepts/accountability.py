import logging
from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# ! Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route('/action', methods=['POST'])
def perform_action():
    user = session.get('user', 'anonymous')
    action = request.json.get('action')
    
    # ! Log the action with the user's information
    logging.info(f"user {user} performed action: {action}")
    
    return jsonify({'message': 'Action performed'})

if __name__ == '__main__':
    app.run(debug=True)

