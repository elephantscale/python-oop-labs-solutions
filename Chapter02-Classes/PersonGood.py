class Person:
    def __init__(self):
       self.__age=1

    def GetAge(self):
        return self.__age

    def SetAge(self, age:int):
        if age<0 or age>120:
            raise Exception("invalid age")
        self.__age=age

def main():
    p=Person()
    p.SetAge(56)
    print(p.GetAge())



if __name__ == "__main__":
    main()
