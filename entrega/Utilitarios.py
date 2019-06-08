from datetime import datetime #pegar o timestemp para realizar a captura da hora que foi criada a transação de cada bloco
from hashlib import sha256 #função para fazer o hash 256


class Utilitarios: 

    def __init__(self):

        timestamp = self.SetTimestamp()

    def SetTimestamp(self): 

        timestamp = round(datetime.utcnow().timestamp())  
        return timestamp

    def set_hash(self, transaction):

        print("data para gerar hash: " + str(transaction) )
        hashTransaction = sha256(transaction.encode()).hexdigest()
        print("return hash da transacao: " + hashTransaction)
        return hashTransaction 

