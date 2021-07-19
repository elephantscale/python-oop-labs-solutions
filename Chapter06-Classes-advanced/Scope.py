def CoolStuff():
    class XClass:
        def FuncA(self):
            print("FuncA")

    obj = XClass()
    obj.FuncA()


def main():
    CoolStuff()

if __name__ == "__main__":
    main()