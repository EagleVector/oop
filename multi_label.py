class bank :

    def transaction(self):

        print("Total transaction value: ")

    def account_opening(self):

        print("This will show your account open status")

    def deposit(self):

        print("This will show you all the deposit you made into your account.")

class HDFC(bank):

    def transfer(self):

        print("This will show all the transfer history.")

class icici(HDFC):
    pass

i = icici()
i.transfer()
i.transaction()
i.deposit()
i.account_opening()

