import time

class Block:
    _no_of_blocks = 0 #keep track of the number of blocks created
    def __init__(self, index, data, previous_hash, current_hash):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.current_hash = current_hash
        self.timestamp = int(time.time())
        Block._no_of_blocks += 1
    @staticmethod
    def size():
        return Block._no_of_blocks