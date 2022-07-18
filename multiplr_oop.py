class bank :

    def transaction(self):

        print("Total transaction value: ")

    def account_opening(self):

        print("This will show your account open status")

    def deposit(self):

        print("This will show you all the deposit you made into your account.")

    def test(self):
        print("This is my test method from my bank class")


class HDFC :

    def transfer(self):

        print("This will show all the transfer history.")

    def test(self):

        print("This is my test method from my HDFC class")

class ineuron:

    def account_ineuron(self):

        print("print account status")

class icici(HDFC, bank, ineuron):
    pass

i = icici()
i.deposit()
i.account_opening()
i.transfer()
i.transaction()
i.test()
i.account_ineuron()