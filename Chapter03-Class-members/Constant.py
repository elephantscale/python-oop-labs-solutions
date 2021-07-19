class Constant:
    ANSWER: int=42
    BAKERSDOZEN: int=13
    DYSTOPIAN:int=1984

def main():
    Constant.ANSWER = 55
    print(Constant.ANSWER)
    print(Constant.BAKERSDOZEN)

if __name__ == "__main__":
    main()