class person2:
    def __init__(self, name, surname, yob):
        self._name = name
        self.__surname = surname
        self.yob = yob

sudh = person2("shudhansu", "kumaar", 1985)
print(sudh._name)
print(sudh._person2__surname)