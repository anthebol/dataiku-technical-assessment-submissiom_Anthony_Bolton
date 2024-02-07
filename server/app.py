from flask import Flask, request, jsonify
from flask_cors import CORS
from c3po.c3po import C3PO  # Ensure this import reflects the correct location of your C3PO class
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
        # Instantiate the C3PO class and calculate the odds
        c3po = C3PO(millennium_falcon_data)
        odds = c3po.calculateOdds(empire_data)
    except KeyError as e:
        # Return an error if the expected keys are not in the JSON
        return jsonify({"error": f"Missing key in JSON data: {str(e)}"}), 400
    except Exception as e:
        # Catch any other exceptions that may occur and return a generic error message
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    # Return the calculated odds if no errors occurred
    return jsonify({"probability": odds})

if __name__ == '__main__':
    app.run(debug=True)
