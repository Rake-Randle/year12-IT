from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# ! Apply rate limiting 
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5 per minute"]
)

@app.route('/resource')
@limiter.limit("10 per minute")
def access_resource():
    return jsonify({'message': 'Resource accessed successfully'})

if __name__ == '__main__':
    app.run(debug=True)