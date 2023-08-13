"""
Напишите класс Point, представляющий собой точку на плоскости, имеющий следующие методы:

- __init__(self, x, y): конструктор, принимающий координаты точки;
- __repr__(self): магический метод, возвращающий строковое представление точки, которое можно использовать для создания нового объекта класса Point;
- __str__(self): магический метод, возвращающий строковое представление точки;
- __add__(self, other): магический метод, который позволяет складывать точки и возвращать новую точку.
"""


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)


point1 = Point(1, 2)
print(f'{repr(point1)}\t->\t{str(point1)}')  # Point(1, 2)

point2 = Point(3, 4)
print(f'{repr(point2)}\t->\t{str(point2)}')  # Point(1, 2)

point3 = point1 + point2
print(f'{point1} + {point2} = {point3}')  # (4, 6)
print(f'{repr(point3)}\t->\t{str(point3)}')  # Point(1, 2)
