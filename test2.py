class person:
    def __init__(self):
        self.name = "Sudhanshu"
        self.surname = "Kumar"
        self.yob = 1989

sudh = person()
#calling a protected variable
print(sudh.name)
#calling a private variable
print(sudh.surname)
print(sudh.yob)
