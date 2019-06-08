from Transacao import Transacao
from MerkTree import MerkTree
from Proof import Proof
from Utilitarios import Utilitarios

class Block: 

    def __init__(self):
        self.blocks = [] 
        self.timestamp = Utilitarios().SetTimestamp()
        self.arrayHashTrasaction = []

    def set_create_genesis_block(self): 
         
        transaction = Transacao('Genesis Block', '', 1000)
        prev_hash = 0
        index = 0
        
        proof = Proof()
        #adicionando o hash retornado o Generate Proof a block
        self.blocks.append(
            # metodo que faz o Proof of Work
            proof.GenerateProof(
                transaction.GetHashTransaction(), self.timestamp , prev_hash, index
            )
        )

    def get_last_chain(self): 
        return self.blocks[:]

    def set_transaction(self, _from, _to, _value):

        transaction = Transacao( _from, _to,_value)
        transaction.printTransacao()
        self.arrayHashTrasaction.append(transaction.GetHashTransaction())
    
    def makeMerkleTree(self, arrayHashTrasaction):
        merkleThree = MerkTree(arrayHashTrasaction)
        merkleThree.calculateMerkTree()
        self.makeProofOfWork(merkleThree.getMerkleTree())

    def makeProofOfWork(self, merkleTree):
        proof = Proof()
        print("[get_last_chain]" , self.get_last_chain())

        # adicionando o hash retornado o Generate Proof a block
        self.blocks.append(
            # metodo que faz o Proof of Work
            proof.GenerateProof(
               merkleTree , self.timestamp , self.get_last_chain(), len(self.blocks)
            )
        )

    def get_blocks(self):
        return self.blocks[:]

def main():

    block = Block()
    
    print('')
    print('-------- GENESIS ---------')
    block = Block()
    block.set_create_genesis_block()

    print('')
    print('-------- 1 block ---------')
    block.set_transaction('from1','to1',10000)
    block.set_transaction('from2','to2',10000)
    # block.set_transaction('from3','to3',10000)
    # block.set_transaction('from4','to4',10000)
    print(block.arrayHashTrasaction)
    block.makeMerkleTree(block.arrayHashTrasaction)

    print('')
    print('-------- 2 block ---------')
    block.set_transaction('from1','to1',20000)
    block.set_transaction('from2','to2',30000)
    # block.set_transaction('from3','to3',20000)
    # block.set_transaction('from4','to4',10000)
    print(block.arrayHashTrasaction)
    block.makeMerkleTree(block.arrayHashTrasaction)

    print('')
    print('------- CHAIN -----------')
    print(block.get_blocks())
   


if __name__ == '__main__':
    main()