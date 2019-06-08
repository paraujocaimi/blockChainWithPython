from hashlib import sha256
from datetime import datetime


class Proof:

    def __init__(self):
        self.blocks = []
        self.set_create_genesis_block()

    def set_create_genesis_block(self):
        _from = 'Genesis Block' 
        _to = ''
        _valor = 10000
        timestamp = datetime.utcnow().timestamp()
        prev_hash = 0
        index = 0
        self.hash_block(
            str(_from+_to+str(_valor)), timestamp, prev_hash, index
        )
    
    def hash_block(self, data, timestamp, prev_hash, index):
        hash = ''
        nonce = 1
        while not self.is_hash_valid(hash):
            block = '{}:{}:{}:{}:{}'.format(
                data, timestamp, prev_hash, index, nonce
            )
            hash = sha256(block.encode()).hexdigest()
            nonce += 1
        print('[nonce]', nonce)
        self.blocks.append(hash)
    
    def get_last_hash(self):
        return self.blocks[-1]
    
    def is_hash_valid(self, hash):
        return hash.startswith('0000')

    def add_Block(self, _from, _to,_valor):
        index = len(self.blocks)
        prev_hash = self.get_last_hash()
        timestamp = datetime.utcnow().timestamp()
        self.hash_block(
            str(_from+_to+str(_valor)), timestamp, prev_hash, index
        )
    
    def get_blocks(self):
        return self.blocks[:]

if __name__ == '__main__':
    blockchain = Proof()

    blockchain.add_Block('from1','to1',10000)
    blockchain.add_Block('from2','to2',10000)
    blockchain.add_Block('from3','to3',10000)

    print(blockchain.get_blocks())