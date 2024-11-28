import time

class Block:
    _no_of_blocks = 0 # keep track of the number of blocks created
    def __init__(self, index, data, previous_hash, current_hash):
        """ Initialize a Block """
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.current_hash = current_hash
        self.timestamp = int(time.time())
        Block._no_of_blocks += 1

    def to_dict(self):
        """ Override __dict__ """
        return {
            'index': self.index,
            'data': self.data,
            'timestamp': self.timestamp,
            'previous_hash': self.previous_hash,
            'current_hash': self.current_hash,
        }

    @staticmethod
    def size():
        """ Return the number of Block instances """
        return Block._no_of_blocks