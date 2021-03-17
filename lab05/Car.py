class Vehicle:
    def __init__(self, vin):
       self.vin=vin

    def GetVin(self):
        return self.vin

class Car(Vehicle):
    def Accelerate(self):
        print("Car accelerating...")

class Truck(Vehicle):
    def Accelerate(self):
        print("Truck accelerating...")

def main():
    p=Car("A1234567890")
    print(p.GetVin())
    p.Accelerate()

    t=Truck("A1234567890")
    print(t.GetVin())
    t.Accelerate()

if __name__ == "__main__":
    main()
