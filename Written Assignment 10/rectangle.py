"""Question 1: Write a simple Rectangle class. It should do the following:
- Accepts length and width as parameters when creating a new instance
- Has a perimeter method that returns the perimeter of the rectangle
- Has an area method that returns the area of the rectangle
- Don't worry about coordinates or negative values, etc.
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimieter(self):
        """Returns the perimeter of the Rectangle."""
        return (self.length * 2) + (self.width * 2)

    def area(self):
        """Returns the area of the Rectangle."""
        return self.length * self.width

    def __repr__(self):
        return ('<Rectangle> length: {}, width: {}, perimeter: {}, area: {}'
                .format(self.length, self.width, self.perimieter(),
                        self.area()))


def main():
    r = Rectangle(4, 7)
    print(r)

    r = Rectangle(25, 76)
    print(r)


if __name__ == '__main__':
    main()