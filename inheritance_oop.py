class car :

    def __init__(self, body, engine, tyre):
        self.body = body
        self.engine = engine
        self.tyre = tyre

    def milage(self):
        print("Milage of this car: 20")

class tata(car):
    pass

indica = tata("iron", "v6", "appolo")
print(indica.milage())