
class Rectangle:

    def __init__(self, base, high) -> None:
        self.base = base
        self.high = high

    def area(self):
        return self.base*self.high

class Square(Rectangle):

    def __init__(self, side) -> None:
        super().__init__(side, side)
    
if __name__ == "__main__":

    rectangle = Rectangle(3,4)

    print()
    print(rectangle.area())
    print()

    square = Square(3)

    print(square.area())
    print()
