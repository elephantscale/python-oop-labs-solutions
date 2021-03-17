class Car:

    def __init__(self):
        self.speed = 5

    def Accelerate(self):
        print("accelerating...")

    def Turn(self):
        print("turning...")
        self.Accelerate()

    def GetSpeed(self):
        print(self.speed)

def main():
    obj=Car()
    print(obj)
    obj.Turn()
    obj.Accelerate()
    obj.GetSpeed()

if __name__ == "__main__":
    main()
