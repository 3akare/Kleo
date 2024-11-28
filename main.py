from classes.Blockchain import Blockchain
from classes.DatabaseConnection import DatabaseConnection

db_connection = DatabaseConnection("mongodb://localhost:27017", "blockchain_db", "blocks")

new_blockchain = Blockchain(db_connection)
new_blockchain.add_block("hello world")
new_blockchain.display_blockchain()

