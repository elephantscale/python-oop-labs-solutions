from dataclasses import dataclass

@dataclass
class AData:
    field1:int=0
    field2:int=1

@dataclass
class BData(AData):
    field3:int=2
    def Total(self):
        return self.field1+self.field2+self.field3

def main():
    obj=BData()

    print(obj)
    print(obj.Total())

if __name__ == "__main__":
    main()