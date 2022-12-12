# Создать классы фигура, прямоугольник, квадрат, круг и эллипс.
# Реализовать методы вычисления площади


enter_a = int(input("Введит сторону или радиус А: "))
enter_b = int(input("Введите сторону или радиус Б: "))

class Figure:
    def __init__(self, name ):
        self.name = name
    def areaFigure(self):
        return
    def area(self):
        print(f"{self.name}, площадь {self.areaFigure()}")

class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__("Rectangle")
        self.side_a = side_a
        self.side_b = side_b
    def areaFigure(self):
        return self.side_a * self.side_b

class Square(Figure):
    def __init__(self, side_a):
        super().__init__("Square")
        self.side_a = side_a
    def areaFigure(self):
        return self.side_a ** 2   

class Circle(Figure):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    def areaFigure(self):
        return 3.14 * (self.radius ** 2)

class Elipse(Figure):
    def __init__(self, radius_big, radius_small):
        super().__init__("Elipse")
        self.radius_big = radius_big
        self.radius_small = radius_small
    def areaFigure(self):
        return 3.14 * self.radius_big * self.radius_small

pl = Rectangle(enter_a,enter_b)
pl.area()

sq = Square(enter_a)
sq.area()

cr = Circle(enter_a)
cr.area()

el = Elipse(enter_a,enter_b)
el.area()