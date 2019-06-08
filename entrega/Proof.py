from hashlib import sha256 #função para fazer o hash 256
from datetime import datetime #pegar o timestemp para realizar a captura da hora que foi criada a transação de cada bloco
from Utilitarios import Utilitarios
from MerkTree import MerkTree
from Utilitarios import Utilitarios
# from Block import Block

class Proof():

    def __init__(self):
        self.timestamp = Utilitarios().SetTimestamp()

    # recebe a ultima posição do merkle root 
    # irá gerar um hash com 4 zeros na frente 
    # O nonce serva para validar se a cadeia está valida
    # Se não for uma cadeira valida irá incrementar o nonce até que seja
    # Quando acha um valor válido ele é adicionado no final da chain - Sendo  o Merkle Root da block
    # def GenerateProof(self, hashTransaction, timestamp, prev_hash, index):

    #     print("hashTransaction " + hashTransaction)
    #     print("timestamp " + str(timestamp))
    #     print("prev_hash " + str(prev_hash))
    #     print("index " + str(index))
        
    #     hash = ''
    #     nonce = 1
    #     while not self.is_valid_proof(hash):
    #         block = '{}'.format(
    #             hashTransaction, timestamp, prev_hash, index, nonce
    #         )
    #         hash = sha256(block.encode()).hexdigest()
    #         #se não acha um bloco com  5 zeros na frene ele incrementa mais  um
    #         nonce += 1
    #         print("[nonce]" , nonce)
    #         print("[Block] " , hash)
    #     #Quantidade de vezes que precisou ser incrementado para achar uma códificação com 4 zeros na frente
    #     print('[nonce]', nonce)
    #     print("[Block] " , hash)
    #     return hash


    def GenerateProof(self, hashTransaction, timestamp, prev_hash, index):

        # print("hashTransaction " + hashTransaction)
        # print("timestamp " + str(timestamp))
        # print("prev_hash " + str(prev_hash))
        # print("index " + str(index))
        
        hash = ''
        nonce = 1
        block = '{}'.format(
            hashTransaction, timestamp, prev_hash, index, nonce
        )
        hash = sha256(block.encode()).hexdigest()
        #se não acha um bloco com  5 zeros na frene ele incrementa mais  um
        nonce += 1
        print("[nonce]" , nonce)
        print("[Block] " , hash)
        
        return hash
    
    def is_valid_proof(self, hash):
        return hash.startswith('0')
