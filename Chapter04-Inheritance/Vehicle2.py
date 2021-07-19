class Vehicle:
    def __init__(self, vin):
        self.vin = vin

    def GetVin(self):
        return self.vin

    def Accelerate(self):
        print("default implementation...")

def main():
    v = Vehicle("B1234567890")
    print(v.GetVin())
    v.Accelerate()

    vv = Car("B1234567891")
    print(vv.GetVin())
    vv.Accelerate()

class Car(Vehicle):
    def Accelerate(self):
        super().Accelerate()
        print("Car accelerating...")


class Truck(Vehicle):
    pass


if __name__ == "__main__":
    main()
