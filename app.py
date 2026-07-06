from flask import Flask, request, send_file
from flask_cors import CORS
import cv2
import numpy as np
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Server Running ✅"

@app.route("/process", methods=["POST"])
def process():

    file = request.files.get("image")

    if not file:
        return "No file", 400

    file_bytes = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if img is None:
        return "Invalid image", 400

    # simple AI processing (test)
    result = cv2.blur(img, (15,15))

    cv2.imwrite("result.png", result)

    return send_file("result.png", mimetype="image/png")

app.run(debug=True)