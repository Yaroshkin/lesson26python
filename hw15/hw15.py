# Создать классы фигура, прямоугольник, квадрат, круг и эллипс.
# Реализовать методы вычисления площади


class Figure:
    def __init__(self, name ):
        self.name = name
    def areaFigure(self):
        return
    def area(self):
        print(f"{self.name}, площадь {self.areaFigure}")

class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__("Rectagle")
        self.side_a = side_a
        self.side_b = side_b
    def areaFigure(self):
        return self.side_a * self.side_b

class Square(Figure):
    def __init__(self):
        super().__init__()

class Circle(Figure):
    def __init__(self):
        super().__init__()

class Elipse(Figure):
    def __init__(self):
        super().__init__()

pl = Rectangle(4,5)
pl.area()