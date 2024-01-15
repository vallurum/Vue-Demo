from flask import Flask, jsonify
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)  

@app.route("/getData")
def get_data():
    csv_file_path = 'resource/data.csv'
    data = []

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)

    # Convert the data to JSON and return
    return jsonify(data)