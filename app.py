from flask import Flask, jsonify

import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
'message': 'Hello from Venkat Raghava DevOps Project!',
'version': os.getenv('APP_VERSION', '1.0.0'),
'status': 'running'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
