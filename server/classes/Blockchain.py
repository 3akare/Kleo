import time

from classes.Block import Block
import hashlib

class Blockchain:
    GENESIS_BLOCK_DATA = "Genesis Block"  # Constant for genesis block data

    def __init__(self, db_connection):
        """Initialize a Blockchain"""
        self._chain = []
        self._db_connection = db_connection
        self.load_from_db()

        if not self._chain:
            self.create_genesis_block()

    def create_genesis_block(self):
        """Create the genesis block and save it in the database"""
        genesis_block = Block(
            index=0,
            data=self.GENESIS_BLOCK_DATA,
            previous_hash="0",
            timestamp=int(time.time())
        )
        self._chain.append(genesis_block)
        self.save_block_to_db(genesis_block)

    def add_block(self, data):
        """Add a new block to the blockchain and save it in the database"""
        previous_block = self._chain[-1]
        new_block = Block(
            index=previous_block.index + 1,
            data=data,
            previous_hash=previous_block.current_hash,
            timestamp=int(time.time())
        )
        self._chain.append(new_block)
        self.save_block_to_db(new_block)

    def load_from_db(self):
        """Load blocks from the database"""
        blockchain_data = self._db_connection.get_all_documents()
        for block_data in blockchain_data:
            self._chain.append(
                Block(
                    block_data["index"],
                    block_data["data"],
                    block_data["previous_hash"],
                    block_data["timestamp"]
                )
            )
            self._chain[-1].set_current_hash(block_data['current_hash'])

    def save_block_to_db(self, block):
        """Save a block to the database"""
        try:
            self._db_connection.insert_one(block.to_dict())
        except Exception as e:
            print(f"Error saving block to database: {e}")

    def display_blockchain(self):
        """Visualize the blockchain"""
        for block in self._chain:
            print(block)

    def blockchain_size(self):
        """Return the number of blocks in the blockchain"""
        return len(self._chain)

    def get_blockchain(self):
        """Return blockchain"""
        return self._chain

    def validate_blockchain(self):
        """Validate the integrity of the blockchain"""
        for i in range(1, len(self._chain)):
            current_block = self._chain[i]
            previous_block = self._chain[i - 1]

            # Check if the current block's hash, and previous block's hash are valid
            if current_block.validate() and previous_block.validate():
                return False

            # Check if the current block's previous_hash matches the previous block's hash
            if current_block.previous_hash != previous_block.current_hash:
                return False

        return True

    @staticmethod
    def create_hash(index, data, previous_hash):
        """Create a hash using the block's attributes"""
        block_string = f"{index}{data}{previous_hash}"
        return hashlib.sha256(block_string.encode("utf-8")).hexdigest()
