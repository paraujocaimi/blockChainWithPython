from Transacao import Transacao

class Block: 

    def __init__(self):
        self.blockchain = [] 

    def create_Genesis(self): 
        transaction = Transacao("Genesis Block", '', 1000)
        self.blockchain.append(transaction.GetHashTransaction())

    def get_last_chain(self): 
        return self.blockchain[-1]

    def add_value(self,transaction):
        self.blockchain.append([transaction])
        print(self.blockchain)

    def send_transaction(self, _to, _from, _value):
        transaction = Transacao( _to, _from, _value)
        self.blockchain.append(transaction.GetHashTransaction())
        print(self.blockchain)


def main():

    block = Block()
    block.create_Genesis()

    #importando transações
    block.send_transaction('to1', 'from1', 30)
    block.send_transaction('to2', 'from2', 10)
    block.send_transaction('to3', 'from3', 40)
    block.send_transaction('to4', 'from4', 50)
    block.send_transaction('to5', 'from5', 170)
    # block2 = Block()


if __name__ == '__main__':
    main()