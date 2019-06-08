from hashlib import sha256 #função para fazer o hash 256
from datetime import datetime #pegar o timestemp para realizar a captura da hora que foi criada a transação de cada bloco
from Utilitarios import Utilitarios


class Transacao:

    def __init__(self, _from, _to, valor):
        
        self._from = _from
        self._to = _to
        self._valor = valor

        #Irá fazer o hash da transacao
        self.hashTransacao = self.SetHashTransacao()
        

    def SetHashTransacao(self):
        util = Utilitarios()

        transacao = str(util.SetTimestamp())+self._from+self._to+str(self._valor)
        # print('[transação para o hash] ', transacao)
        hash = sha256(transacao.encode()).hexdigest()         
         
        return hash

    def GetHashTransaction(self):
        return self.hashTransacao

    def printTransacao(self):
        print ("[_from: " + str(self._from) + " _to: " + str(self._to) + " valor: " + str(self._valor) +" Hash: " + str(self.hashTransacao) +"]")

    