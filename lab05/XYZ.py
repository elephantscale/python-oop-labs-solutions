class ZClass:
    def __init__(self, param3):
        pass

class YClass(ZClass):
    def __init__(self, param2, param3):
        super().__init__(param3)

class XClass(YClass):
    def __init__(self, param1, param2, param3):
        super().__init__(param2, param3)

def main():
    obj=XClass(1, 2, 3)
    print("No output, but run in the debugger")

if __name__ == "__main__":
    main()
