class Person:
    def __init__(self):
        self.__age = 1

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        if age < 0 or age > 120:
            raise Exception("invalid age")
        self.__age = age


def main():
    p = Person()
    p.age = 56
    print(p.age)

if __name__ == "__main__":
    main()