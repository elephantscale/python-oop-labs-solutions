class Person:
    def __init__(self):
        self.__age = 1

    def age_getter(self):
        return self.__age

    def age_setter(self, age: int):
        if age < 0 or age > 120:
            raise Exception("invalid age")
        self.__age = age

    age = property(fget=age_getter, fset=age_setter)


obj = Person()
obj.age = 42
print(obj.age)
