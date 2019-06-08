import hashlib
from hashlib import sha256 #função para fazer o hash 256

# site para verificar hash
# https://timestampgenerator.com/tools/sha256-generator 

#Fazer o calculo do hash do block para gerar o Proof of work
class MerkTree: 

        def __init__(self, _arrayHash):
                self.arrayHash = _arrayHash

        #está função serve para verificar se a quantidade hash retornado de todas as transações
        # são impares ou pares, assim para cada condicionamente ele irá para uma função
        # geradora de hash diferene
        def calculateMerkTree(self):
                # print("calculateMerkTree")
                # print(len(self.arrayHash))
                # print('')
                # print("[array das transações] " , str(self.arrayHash))

                if(len(self.arrayHash) == 1):
                        # print("unica transação: " + str(len(self.arrayHash)))
                        return self.arrayHash

                #sendo o array de hash das transações pares
                elif(len(self.arrayHash)%2 == 0):
                        # print("Número par: " + str(len(self.arrayHash)))
                        self.merkleTreePar()
                        # self.getMerkleTree()
                #se ele for impar, ele irá duplicar a ultima transação e irá passar pelo laço novamente
                # para assim gerar o merkle tree
                else:
                #        print("Número ímpar: " + str(len(self.arrayHash)))
                       self.merkleTreeImpar()
                
                return self.arrayHash

        def merkleTreePar(self):

                i=0
                while i < len(self.arrayHash):                        
                         
                        #se não tiver igual ao tamanho do hash
                        # irá realizar a junção das transações
                        # print("Transação "  +str(i) + " " + self.arrayHash[i])
                        elem1 = self.arrayHash[i]
                        #verifica se o i está do mesmo tamanho que o tamanho do hash de transações
                        i+=1 
                        if (i >= len(self.arrayHash)):
                                pass
                        else:
                                # print("Transação " + str(i) + " " + self.arrayHash[i])
                                elem2 = self.arrayHash[i]
                                block = format(
                                    str(elem1)+str(elem2)   
                                )
                                # print("elem1 + elem2")
                                # print(block)
                                #pego o bloco criado e codifico de hex para sha256
                                hash = sha256(block.encode()).hexdigest()
                                self.arrayHash.append(hash)   
                                i+=1  
                print('')                 
                print("[Merkle Three]  " + str(self.arrayHash))
                return self.arrayHash

        def merkleTreeImpar(self):

                lenf = len(self.arrayHash)
                self.arrayHash.append(self.arrayHash[lenf-1])
                self.calculateMerkTree()

        def getMerkleTree(self):  
                print('')                  
                print("última posição do merkle tree:  " + self.arrayHash[len(self.arrayHash)-1])            
                return self.arrayHash[len(self.arrayHash)-1]

               

