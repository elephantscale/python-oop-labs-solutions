class Base1:
    def FuncA(self):
        print("Base1::FuncA")

class Base2:
    def FuncA(self):
        print("Base2::FuncA")

class Child(Base1, Base2):
    pass

def main():
    obj=Child()
    obj.FuncA()

if __name__ == "__main__":
    main()
