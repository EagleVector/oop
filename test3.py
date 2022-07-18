import test4
from utils.utill1 import person2
obj5 = person2("Niall", "Horran" , 1994)
print(obj5._name)
print(obj5._person2__surname)
print(obj5.yob)
obj3 = test4.person1("zayn", "malik", 1995)
print(obj3._name)
print(obj3._person1__surname)
print(obj3.yob)

class person:

    _name = "shubham"
    __surname = "kashyap"
    yob = 1996

    def _age(self, current_yr):
        return current_yr - self.yob

    def __age1(self, current_yr):
        return current_yr - self.yob

obj = person()

print(obj.yob)
print(obj._age(2022))
print(obj._person__age1(2022))


class employee(person):
    _name = "sudhanshu"
    __surname = "singh"
    yob = 1990

obj1 = employee()
print(obj1._name)
print(obj1.yob)
print(obj1._person__surname)

print(obj1.yob)
print(obj1._age(2022))
print(obj1._person__age1(2022))
