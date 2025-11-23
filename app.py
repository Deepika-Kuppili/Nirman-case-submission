
from flask import Flask, request, jsonify
import json, os
app = Flask(__name__)
@app.route("/")
def home():
    return "Nirmaan Scoring API is running. Use POST /score to evaluate transcripts."

@app.route('/score', methods=['POST'])
def score():
    payload = request.get_json()
    # This is a placeholder. The real scorer is provided as score.py + scoring_result.json for sample.
    # For production, replace with the functions in scoring script.
    return jsonify({'message':'Use the included scoring script (score.py) to reproduce scoring. This endpoint is a placeholder.'})
if __name__ == '__main__':
    app.run(debug=True, port=5000)
