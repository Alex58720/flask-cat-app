from flask import Flask, render_template, jsonify, request
import random
import os
from logger import setup_logger

app = Flask(__name__)

# Set up logger
logger = setup_logger()

@app.route('/')
def index():
    gifs_dir = os.path.join(app.static_folder, 'gifs')
    gifs = [f for f in os.listdir(gifs_dir) if f.endswith('.gif')]
    if gifs:
        random_gif = random.choice(gifs)
        url = f'/static/gifs/{random_gif}'
    else:
        url = ''
    return render_template('index.html', url=url)

@app.route('/welcome', methods=['GET'])
def welcome():
    """
    Returns a welcome message
    """
    logger.info(f"Request received: {request.method} {request.path}")
    return jsonify({'message': 'Welcome to the Flask Cat App!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
