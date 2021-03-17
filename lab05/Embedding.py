class Vehicle:
    def __init__(self, vin):
        self.vin = vin

    def GetVin(self):
        return self.vin


class Engine:
    def Start(self):
        print("start engine...")


class Car(Vehicle):
    def __init__(self):
        self.__engine = Engine()

    def Start(self):
        self.__engine.Start()
        print("car started...")

def main():
    obj = Car()
    obj.Start()

if __name__ == "__main__":
    main()
