from figure.Shape import Shape


class Circle(Shape):
    PI = 3.1415926535

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius ** 2
