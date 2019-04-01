import hashlib
import datetime as date

class Transacao:

    def __init__(self, _from, _to, valor):
        
        self._from = _from
        self._to = _to
        self.valor = valor
        self.hashTransacao = self.calculateHashTransacao()

    
    def calculateHashTransacao(self):
        sha = hashlib.sha256()
        sha.update(str(self._from).encode('utf-8') +
                   str(self._to).encode('utf-8') +
                   str(self.valor).encode('utf-8'))
        return sha.hexdigest()

    def printBlock(self):
        print ("_from: " + str(self._from))
        print ("_to: " + str(self._to))
        print ("valor: " + str(self.valor))
        print ("Hash: " + str(self.hashTransacao))
        print ("---------------")