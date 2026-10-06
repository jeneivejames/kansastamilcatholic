from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Kansas Tamil Catholic Community</h1><p>Test - App is working!</p>'

@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)