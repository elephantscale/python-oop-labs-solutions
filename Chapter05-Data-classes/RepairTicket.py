from dataclasses import dataclass
@dataclass
class RepairTicket:
    id:str=""
    desc:str=""
    priority:int=5

def main():
    t1=RepairTicket("A123",
                    "This is description",
                    priority=7)
    print(t1)

if __name__ == "__main__":
    main()