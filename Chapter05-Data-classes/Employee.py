from dataclasses import dataclass
@dataclass
class Employee:
    Name:str=""
    Age:int=0

def main():
    bob=Employee()
    bob.Name="Bob"
    bob.Age=56
    bob2 = Employee()
    bob2.Name = "Bob"
    bob2.Age = 56

    if bob == bob2:
        print("equal")
    else:
        print("not equal")


if __name__ == "__main__":
    main()



