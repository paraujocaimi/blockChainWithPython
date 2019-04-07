import datetime as date
from Block import *
from Transacao import *
from MerkTree import *

class BlockChain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]

    def createGenesisBlock(self):
        return Block(0, date.datetime.now(), "Genesis Block", "", "")

    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]

    def addBlock(self, newBlock, merkleRoot):
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.hash = newBlock.calculateHash()
        newBlock.merkleRoot = merkleRoot
        self.chain.append(newBlock)

    def isChainValid(self):
        for i in range (1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i-1]
            # checks whether data has been tampered with
            if currentBlock.hash != currentBlock.calculateHash():
                return False
            if currentBlock.previousHash != previousBlock.hash:
                return False
        return True

    def printBlockChain(self):
        for i in range(0, len(self.chain)):
            self.chain[i].printBlock()

def main():
    
    scilaCoin = BlockChain()
    
    #Crio um array para receber apenas o hash de cada transação
    arrayHash = []

    transacaoBlock = [
        Transacao('Priscila', 'Brayan', 30),
        Transacao('Patricia','Vitor', 10),
        Transacao('Joana', 'Clarissa', 40),
        Transacao('João', 'Karine', 60)
    ]

    print("=== TRANSAÇÕES ===")
    print(" ")
    for i in transacaoBlock:
        # print(i.printBlock())
        # adicionando o hash da transação no array de hash 
        arrayHash.append(i.hashTransacao)

    # Passo este array que contem apenas o hash para a classe que irá 
    # tanto faz o maket tree quando adiciona-los ao mesmo array
    merkTree = MerkTree(arrayHash)
    merkTree.calculateMerkTree()
    merkTree.pegarHashMerkleRoot()
    
    # Aqui vou criar o meu primeiro bloco da Chain
    # scilaCoin.addBlock(Block(1, date.datetime.now(),transacaoBlock),merkTree.pegarHashMerkleRoot())
    # scilaCoin.addBlock(Block(2, date.datetime.now(),transacaoBlock),merkTree.pegarHashMerkleRoot())
    # scilaCoin.addBlock(Block(3, date.datetime.now(),transacaoBlock),merkTree.pegarHashMerkleRoot())
    # scilaCoin.addBlock(Block(4, date.datetime.now(),transacaoBlock),merkTree.pegarHashMerkleRoot())

    # scilaCoin.printBlockChain()

if __name__ == '__main__':
    main()
