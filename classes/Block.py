import time
import hashlib

class Block:
    _no_of_blocks = 0  # Keep track of the number of blocks created

    def __init__(self, index, data, previous_hash):
        """Initialize a Block"""
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = int(time.time())
        self.current_hash = self.calculate_hash()
        Block._no_of_blocks += 1

    def calculate_hash(self):
        """Calculate the hash of the block"""
        hash_input = f"{self.index}{self.data}{self.timestamp}{self.previous_hash}"
        return hashlib.sha256(hash_input.encode()).hexdigest()

    def to_dict(self):
        """Return a dictionary representation of the block"""
        return {
            'index': self.index,
            'data': self.data,
            'timestamp': self.timestamp,
            'previous_hash': self.previous_hash,
            'current_hash': self.current_hash,
        }

    def __str__(self):
        """String representation of the block"""
        return f"Block(index={self.index}, current_hash={self.current_hash[:8]}...)"

    @staticmethod
    def get_block_count():
        """Return the number of Block instances"""
        return Block._no_of_blocks

    def validate(self):
        """Validate the block's hash"""
        return self.current_hash == self.calculate_hash()
