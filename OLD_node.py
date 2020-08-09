from blockchain import Blockchain
from utility.verification import Verification
from uuid import uuid4
from wallet import Wallet



class Node:
    def __init__(self):   
        #self.wallet = Wallet()
        #self.wallet.create_keys()
        self.wallet = Wallet()
        self.wallet.create_keys()
        self.blockchain = Blockchain(self.wallet.public_key)

    def get_transaction_value(self):
        tx_recipient = input('Enter the recipient of the transaction: ')
        tx_amount =  float(input('Your Transaction amount please: '))
        return tx_recipient,tx_amount

    def print_blockcahin_elements(self):
        for block in self.blockchain.chain:
            print('Outputting Block..')
            print(block)
        else:
           print('-'*20)

    def get_user_choice(self):
        user_input = input('Your Choice: ')
        return user_input

    def listen_for_input(self):

        waiting_for_input = True

        while waiting_for_input:
            print('Please choose:')
            print('1: add a new transaction value')
            print('2: Mine a new block')
            print('3: output the blockchain blocks')
            print('4: Check Transaction Validity')
            print('5: Create Wallet.')
            print('6: Load Wallet.')
            print('7: Save Keys.')
            print('q: Quit ')

            user_choice = self.get_user_choice()

            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient,amount = tx_data
                signature = self.wallet.sign_transaction(self.wallet.public_key,recipient,amount)
                if self.blockchain.add_transaction(recipient,self.wallet.public_key,signature,amount=amount):
                   print('Added Transaction!')
                else:
                  print('Tansaction Failed!')
                   
                print(self.blockchain.get_open_transactions())

            elif user_choice =='2':
                if not self.blockchain.mine_block():
                   print('Minig Failed..Got no wallet?')
            elif user_choice =='3':
                self.print_blockcahin_elements()
            elif user_choice =='4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(),self.blockchain.get_balance):
                   print('All Transactions are Valid!')
                else:
                   print('There are Invalid Transaction')
            elif user_choice =='5': 
                 self.wallet.create_keys()
                 self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice =='6':
                 self.wallet.load_keys()
                 self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice =='7':
                 self.wallet.save_keys()
            elif user_choice =='q':
                waiting_for_input = False
            else:
               print('it was a invalid input! please a valid input....')

            if not Verification.verify_chain(self.blockchain.chain):
                self.print_blockcahin_elements()
                print('Invalid Blockchian!')
                break
            print('Balance of {} :{:6.2f}'.format(self.wallet.public_key,self.blockchain.get_balance()))
        else:
           print('user_left')
        print('Done!')

if __name__ == '__main__':
   node = Node() 
   node.listen_for_input()


