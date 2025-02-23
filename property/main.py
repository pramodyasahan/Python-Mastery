class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            print("width must be positive")

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            print("height must be positive")

    @width.delete
    def width(self):
        del self._width
        print("width deleted")

    @height.delete
    def height(self):
        del self._height
        print("height deleted")


rectangle = Rectangle(100, 120)
rectangle.width = 150
print(rectangle.width)
