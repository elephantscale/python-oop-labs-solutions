from dataclasses import dataclass


class Factorial:
    def __init__(self):
        self.__value = 1

    def __call__(self, value: int):
        self.__value = value
        for item in range(1, value):
            self.__value = self.__value * item
        return self.__value


def main():
    obj = Factorial()
    print(obj(5))
    if callable(obj):
        print("object is callable")

if __name__ == "__main__":
    main()