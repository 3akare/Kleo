from classes.Block import Block
import hashlib
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block(
            len(self.chain),
            "Genesis Block",
            Blockchain.create_hash("Genesis Block"),
            Blockchain.create_hash("Genesis Block"),
        )

    def add_block(self, data):
        index = len(self.chain)
        new_block = Block(
            index,
            data,
            self.chain[-1].current_hash,
            Blockchain.create_hash(data))
        self.chain.append(new_block)

    def create_genesis_block(self, index, data, previous_hash, current_hash):
        genesis_block = Block(index, data, previous_hash, current_hash)
        self.chain.append(genesis_block)

    def display_blockchain(self):
        for block in self.chain:
            print("==>", block.__dict__)

    @staticmethod
    def create_hash(data):
        block_string = f"{data}{int(time.time())}"
        return hashlib.sha256(block_string.encode('utf-8')).hexdigest()
