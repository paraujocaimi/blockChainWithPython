from hashlib import sha256 #função para fazer o hash 256
from datetime import datetime #pegar o timestemp para realizar a captura da hora que foi criada a transação de cada bloco


class Transacao:

    def __init__(self, _from, _to, valor):
        
        self._from = _from
        self._to = _to
        self._valor = valor

        #irá setar a hora da transacao
        self.timestamp = self.SetTimestamp()

        #Irá fazer o hash da transacao
        self.hashTransacao = self.SetHashTransacao()
        
        #irá adicionar o hash de todas as transações em uma variavel para usa-la em outras classes
        self.arrayHash = self.SetMerkleRoot('')

    # realizando um metodo que pega a hora exata da transação
    def SetTimestamp(self): 

        timestamp = round(datetime.utcnow().timestamp())  
        return timestamp

    # com este metodo ele irá fazer o hash dos dados da transação 
    # e juntamente fazer o proof e adicionar o timestamp
    def SetHashTransacao(self):
       
        transacao = '{}{}{}{}'.format(self.timestamp,self._from,self._to,self._valor)
        print("transacao:" + transacao)
        hash = sha256(transacao.encode()).hexdigest()
        # return transacao
        
        print("_from: " + self._from)
        print("_to: " + str(self._to))
        print("_valor: " + str(self._valor))
        
        print("Print da transação: " + transacao)
        print("Hash: " + hash)
            
         
        return hash

    def GetHashTransaction(self):
        return self.hashTransacao

    def SetMerkleRoot(self,transacaoBlock):
        array = []

        for i in transacaoBlock:
            # print(i.hashTransacao) 
            array.append(i.hashTransacao)

        print(array)
        return array


    def GetMerkRoot(self,arrayHash):

        print("aqui")
        print(self.arrayHash)
        for i in self.arrayHash:
            print("aqui2"+ i)
            print(self.arrayHash[i])

    def printTransacao(self):
        print ("[_from: " + str(self._from) + " _to: " + str(self._to) + " valor: " + str(self._valor) +" Hash: " + str(self.hashTransacao) +"]")


# def main():

#     #instanciando a classe
#     transacao = Transacao('','','')

#     #Chamando o metodo para buscar as transações
#     #E imprimi as transações que foram adicinadas ao bloco
#     # [_from: Envia01 _to: Recebedor01 valor: 30 Hash: 4b3e97faddc6c21df2de0b271641465b6c67ad50be3bdd49b8b8769267e1b91c]
#     transacaoBlock = transacao.SetTrasacao()
#     transacao.SetHashTransacao(transacaoBlock)
    
#     # Adicionando todos os hashs individuais de cada transção 
#     # para um array e criar o MerkleRoot da block
#     # imprimir o array com o todos os hash das transações
#     # transacao.SetMerkleRoot(transacaoBlock)

#     #exibir o hash das transações
#     # transacao.GetMerkRoot('')


# if __name__ == '__main__':
#     main()