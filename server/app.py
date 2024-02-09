from flask import Flask, request, jsonify
from flask_cors import CORS
from c3po.c3po import C3PO
import json

app = Flask(__name__)
CORS(app)

@app.route('/calculateOdds', methods=['POST'])
def calculateOdds():
    if 'millennium-falcon' not in request.files or 'empire' not in request.files:
        return jsonify({"error": "Missing files"}), 400

    millennium_falcon_file = request.files['millennium-falcon']
    empire_file = request.files['empire']

    if millennium_falcon_file.filename == '' or empire_file.filename == '':
        return jsonify({"error": "No selected files"}), 400

    try:
        millennium_falcon_data = json.load(millennium_falcon_file)
        empire_data = json.load(empire_file)
    except json.JSONDecodeError as e:
        return jsonify({"error": f"Invalid JSON content: {str(e)}"}), 400

    try:
        c3po = C3PO(millennium_falcon_data)
        odds = c3po.calculateOdds(empire_data)
    except KeyError as e:
        return jsonify({"error": f"Missing key in JSON data: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    return jsonify({"probability": odds})

if __name__ == '__main__':
    app.run(debug=True, port=8081)
