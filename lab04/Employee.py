class Employee:
    __employer = ""

    @classmethod
    def GetEmployer(cls):
        return cls.__employer

    @classmethod
    def SetEmployer(cls, employer: str):
        cls.__employer = employer

    def __init__(self, name: str):
        self.name = name

    def GetName(self):
        return self.name


def main():
    Employee.SetEmployer("ABC Company")
    bob = Employee("Bob Jones")
    sally = Employee("Sally Rider")
    print(bob.GetEmployer() + ":", bob.GetName())
    print(sally.GetEmployer() + ":", sally.GetName())

if __name__ == "__main__":
    main()