"""
Notes from the course:
Isolation - isolating into a sandbox, developers can preent potential threats from spreading, reducing risk of malware infection
Testing - allows developers to test different code whilst being controlled
Mitigating Risks - If a sandbox is compromised, it only effects the enviroment
"""
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/run_code', methods=['POST'])
def run_code():
    code = request.json.get('code')
    
    try:
        # * run the code in a sandboxed enviroment
        result = subprocess.run(['python3', '-c', code], capture_output=True, text=True, timeout=5)
        return jsonify({'output': result.stdout, 'error': result.stderr})
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Code execution times out'})
    
if __name__ == '__main__':
    app.run(debug=True)