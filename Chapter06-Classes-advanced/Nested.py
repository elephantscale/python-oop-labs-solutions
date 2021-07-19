class Car:
    def __init__(self):
        self.__transmission = self.Transmission()
        self.__alternator = self.Alternator()

    def Start(self):
        print("car starting..")
        self.__transmission.Start()
        self.__alternator.Start()

    class Transmission:
        def Start(self):
            print("transmission running")

    class Alternator:
        def Start(self):
            print("alternator running")


def main():
    obj = Car()
    obj.Start()

if __name__ == "__main__":
    main()