import hashlib


class MerkTree: 

        def __init__(self, arrayHash):
                self.arrayHash = arrayHash
                self.arrayMerkTree = self.arrayHash
                self.merkleRoot = self.pegarHashMerkleRoot()

        def calculateMerkTree(self):

                # hash12 = str(self.arrayHash[0])+str(self.arrayHash[1])
                # hash34 = str(self.arrayHash[2])+str(self.arrayHash[3])

                # sha12 = hashlib.sha256()
                # sha12.update(str(hash12).encode('utf-8'))
                # self.arrayHash.append(sha12.hexdigest())

                # sha34 = hashlib.sha256()
                # sha34.update(str(hash34).encode('utf-8'))
                # self.arrayHash.append(sha34.hexdigest())


                # sha1234 = hashlib.sha256()
                # hash34 = str(self.arrayHash[4])+str(self.arrayHash[5])
                # sha1234.update(str(hash34).encode('utf-8'))
                # self.arrayHash.append(sha1234.hexdigest())
                
                # MerkTree.printMerkTree(self)

                sha = hashlib.sha256()
                i=0
                while i < len(self.arrayHash):
                        elem1 = (self.arrayHash[i])
                        print("Posição: " + str(i) + " Hash: " + str(elem1))
                        
                        i+=1

                        if (i>= len(self.arrayHash)):
                                print("Acabou aqui!!!: " + str(i))
                                pass
                        else:
                                elem2 = (self.arrayHash[i])
                                print("Posição: " + str(i) + " Hash: " + str(elem2))
                                i+=1 

                                no = str(elem1)+str(elem2)
                                print("no: " + str(elem1)+str(elem2))
                                sha.update(str(no).encode('utf-8'))
                                self.arrayHash.append(sha.hexdigest())      
                
                MerkTree.printMerkTree(self)

                return self.arrayHash

        def pegarHashMerkleRoot(self): 
                posicao = len(self.arrayHash)
                print("--- MERKLE ROOT ---")
                print(str(self.arrayHash[posicao-1]))
                print(" ")
                merkleRoot = str(self.arrayHash[posicao-1])
                return merkleRoot

        def printMerkTree(self):
                print ("--- MERK TREE ---")
                print ("Array Hash: " + str(self.arrayMerkTree))
                print (" ")

