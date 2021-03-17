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
    cars=[Car("A123456890"), Car("B123456890"),
          Truck("C123456890"), Truck("D123456890"),
          Car("E123456890")]
    for car in cars:
        car.Accelerate() # polymorphic site

if __name__ == "__main__":
    main()