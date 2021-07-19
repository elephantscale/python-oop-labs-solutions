from dataclasses import dataclass

@dataclass(frozen=True)
class Constant:
    ANSWER: int=42
    BAKERSDOZEN: int=13
    DYSTOPIAN:int=1984

def main():
    obj=Constant()
    # This should give an error
    obj.ANSWER=67
    print(obj.ANSWER)
    print(obj.BAKERSDOZEN)

if __name__ == "__main__":
    main()
