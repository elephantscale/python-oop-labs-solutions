
class Base1:
    def __init__(self):
        print("base1")

class Base2:
    def __init__(self):
        print("base2")

class Inner:
    def __init__(self):
        print("embedded")

class Child(Base1, Base2):
    def __init__(self):
        self.inner=Inner()
        print("child")

def main():
    obj=Child()

if __name__ == "__main__":
    main()
