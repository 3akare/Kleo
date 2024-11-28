from classes.Block import Block
import hashlib
import time

class Blockchain:
    def __init__(self, db_connection):
        """ Initialize a Blockchain """
        self._chain = []
        self._db_connection = db_connection
        self.load_from_db()

        if len(self._chain) == 0:
            self.create_genesis_block(
                len(self._chain),
                "Genesis Block",
                Blockchain.create_hash("Genesis Block"),
                Blockchain.create_hash("Genesis Block"),
            )

    def create_genesis_block(self, index, data, previous_hash, current_hash):
        """ Create a genesis block. The first block in the blockchain, and save the update in the database"""
        genesis_block = Block(index, data, previous_hash, current_hash)
        self._chain.append(genesis_block)
        self.save_block_to_db(genesis_block)

    def add_block(self, data):
        """ Add more block of class Block to Blockchain, and save the update in the database """
        index = self._chain[-1].index + 1
        new_block = Block(
            index,
            data,
            self._chain[-1].current_hash,
            Blockchain.create_hash(data))
        self._chain.append(new_block)
        self.save_block_to_db(new_block)

    def load_from_db(self):
        """ Load blocks from the db """
        blockchain_data = self._db_connection.find_all()
        for block_data in blockchain_data:
            self._chain.append(
                Block(
                  block_data['index'],
                  block_data['data'],
                  block_data['previous_hash'],
                  block_data['current_hash'],
                )
            )

    def save_block_to_db(self, block):
        """ Save block in the db """
        self._db_connection.insert_one(block.to_dict())

    def display_blockchain(self):
        """ Visualise blockchain """
        for block in self._chain:
            print("==>", block.__dict__)

    def blockchain_size(self):
        """ No. of blocks in blockchain. It should always be the same as Block.size()"""
        return len(self._chain)

    @staticmethod
    def create_hash(data):
        """ Create hash using the block data, and timestamp """
        block_string = f"{data}{int(time.time())}"
        return hashlib.sha256(block_string.encode('utf-8')).hexdigest()

