class Person:
    def __init__(self):
       self.__age=1

	# ...

    def __del__(self):
        print("cleaning up...")

def main():
    p=Person()
    p.age=56
    print(p.age)
    del p

if __name__ == "__main__":
    main()
