from collections import OrderedDict
from utility.printable import Printable
from wallet import Wallet

class Transaction(Printable):
    def __init__(self,sender,recipient,signature,amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature


    def to_ordered_dict(self):
        return OrderedDict([('sender',self.sender),('recipient',self.recipient),('amount',self.amount)])

