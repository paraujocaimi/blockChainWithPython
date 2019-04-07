import hashlib
import datetime as date


# Block Object
class Block:
    def __init__(self, index, timestamp, transacao, previousHash=' ', merkleRoot = ''):
        self.index = index
        self.timestamp = timestamp
        self.dado = transacao
        self.previousHash = previousHash
        self.hash = self.calculateHash()
        self.merkleRoot = merkleRoot

    def calculateHash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(date.datetime.now()).encode('utf-8') +
                   str(self.dado).encode('utf-8') +
                   str(self.previousHash).encode('utf-8'))
        return sha.hexdigest()

    def printBlock(self):
        print ("Block #" + str(self.index))
        print ("Merkle Tree: "  + str(self.merkleRoot))
        print ("Trasanção: " + str(self.dado))
        print ("Block Hash: " + str(self.hash))
        print ("Block Previous Hash: " + str(self.previousHash))
        print ("---------------")