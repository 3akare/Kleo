from flask import Flask, jsonify, request
from flask_cors import CORS
from classes.Blockchain import Blockchain
from classes.DatabaseConnection import DatabaseConnection
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, origins='*')

mongo_uri = os.getenv("MONGO_URI")

db_connection = DatabaseConnection(mongo_uri, "blockchain_db", "blocks")
blockchain = Blockchain(db_connection)

@app.route("/", methods=["GET"])
def home():
    """Home"""
    return jsonify({"location": "blockchain"}), 200

@app.route("/blockchain", methods=["GET"])
def get_blockchain():
    """Get the entire blockchain"""
    chain_data = [block.to_dict() for block in blockchain.get_blockchain()]
    return jsonify({"blockchain": chain_data, "length": blockchain.blockchain_size()}), 200

@app.route("/add_block", methods=["POST"])
def add_block():
    """Add a block to the blockchain"""
    data = request.json
    if not data or "data" not in data:
        return jsonify({"error": "Invalid input, 'data' is required"}), 400

    blockchain.add_block(data["data"])
    return jsonify({"message": "Block added successfully!", "data": data["data"]}), 201

@app.route("/validate", methods=["GET"])
def validate_blockchain():
    """Validate the blockchain"""
    is_valid = blockchain.validate_blockchain()
    return jsonify({"is_valid": is_valid}), 200

@app.route("/block/<int:index>", methods=["GET"])
def get_block(index):
    """Get a block by index"""
    if index < 0 or index >= blockchain.blockchain_size():
        return jsonify({"error": "Block index out of range"}), 404

    block = blockchain.get_blockchain()[index]
    return jsonify(block.to_dict()), 200

# Run Flask App
if __name__ == "__main__":
    app.run(debug=True, port=8080)
