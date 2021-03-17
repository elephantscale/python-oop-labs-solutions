class Employee:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Salaried(Employee):

    def __init__(self, name: str, wage: float):
        super().__init__(name)
        self.__wage = wage


class Hourly(Employee):

    def __init__(self, name: str, hourly: float):
        super().__init__(name)
        self.__hourly = hourly

def main():
    bob = Salaried("Bob", 10000)
    sally = Hourly("Sally", 50)
    print(bob.name)
    print(sally.name)


if __name__ == "__main__":
    main()


