class Vehicle:
    def __init__(self, vin):
        self.vin = vin

    def GetVin(self):
        return self.vin


class Car(Vehicle):
    def Accelerate(self):
        print("Car accelerating...")


class Truck(Vehicle):
    def Accelerate(self):
        print("Truck accelerating...")


def main():
    v = Vehicle("B1234567890")
    # v.Accelerate()
    print(v.GetVin())

if __name__ == "__main__":
    main()