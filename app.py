```python
from flask import Flask, request, jsonify
from database import Database
from image_processing import process_image
from openai_api import generate_critique
import numpy as np
import cv2
import requests
from PIL import Image
import io

app = Flask(__name__)
db = Database()

@app.route('/')
def home():
    return "Welcome to AI Art Critic!"

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    image = Image.open(file.stream)  # Open image file
    processed_image = process_image(image)  # Process image
    critique = generate_critique(processed_image)  # Generate critique
    return jsonify(critique)

@app.route('/compare', methods=['POST'])
def compare():
    file1 = request.files['file1']
    file2 = request.files['file2']
    image1 = Image.open(file1.stream)
    image2 = Image.open(file2.stream)
    processed_image1 = process_image(image1)
    processed_image2 = process_image(image2)
    comparison = generate_critique(processed_image1, processed_image2)
    return jsonify(comparison)

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    user = db.get_user(username)
    return jsonify(user)

@app.route('/user', methods=['POST'])
def create_user():
    user_data = request.get_json()
    db.create_user(user_data)
    return jsonify({'message': 'User created successfully!'})

@app.route('/user/<username>', methods=['PUT'])
def update_user(username):
    user_data = request.get_json()
    db.update_user(username, user_data)
    return jsonify({'message': 'User updated successfully!'})

@app.route('/user/<username>', methods=['DELETE'])
def delete_user(username):
    db.delete_user(username)
    return jsonify({'message': 'User deleted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
```
