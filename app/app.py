from flask import Flask,request, jsonify
from PIL import Image
from modelUse import generate_palette

app = Flask(__name__)

@app.route("/generate", methods=['GET'])
def generate():    
    return jsonify(generate_palette())

@app.route("/generate-by-picture", methods=['POST'])
def upload_file():
    print("sdfsdfsd")
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    try:
        image = Image.open(file.stream)
        return ["000000", "000000", "000000", "000000", "000000"]
    except Exception as e:
        return []
    
    

if (__name__) == "__main__":
    app.run(port=8081)