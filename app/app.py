from flask import Flask, jsonify
from modelUse import generate_palette

app = Flask(__name__)

@app.route("/generate", methods=['GET'])
def generate():    
    return jsonify(generate_palette())

if (__name__) == "__main__":
    app.run(port=8081)