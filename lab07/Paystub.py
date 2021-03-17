from dataclasses import dataclass


@dataclass
class Paystub:
    paystub_id: str = ""
    employee_id: str = ""
    amount: int = 0


def main():
    pay1 = Paystub("A456", "EMPL1", 5000)
    pay2 = Paystub("C136", "EMPL2", 4500)
    print(pay1)
    print(pay2)


if __name__ == "__main__":
    main()
