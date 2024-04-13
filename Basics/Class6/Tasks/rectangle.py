# Create a class called "Rectangle" with attributes for length and width.
# Add a method to the Rectangle class that calculates and returns the area.
# Create a subclass of Rectangle called "Square" that automatically sets the length and width to be equal.
# Add a method to the Square class that calculates and returns the perimeter.

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)      # Set length and width to be the same for a square

    def perimeter(self):
        return 4 * self.length                 # Perimeter of a square is dec times the length (since all sides are equal)


length = float(input("Please enter the length: "))
width = float(input("Please enter the width: "))
rectangle = Rectangle(length, width)
print("Rectangle area is ",rectangle.area())
square = Square(length)
print("Square perimeter is ",square.perimeter())