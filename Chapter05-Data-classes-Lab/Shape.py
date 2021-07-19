from dataclasses import dataclass

@dataclass
class Shape:
    Type:""
    Width:0
    Height:0


def main():
    rect1=Shape("Rectangle", 5, 10)
    rect2=Shape("Rectangle", 5, 10)
    if rect1==rect2:
        print("Rectangles equal")
    else:
        print("Rectangles not equal")

if __name__ == "__main__":
    main()