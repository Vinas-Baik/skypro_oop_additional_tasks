"""
Напишите класс Rectangle, имеющий следующие методы:

- __init__(self, width, height): конструктор, принимающий ширину и высоту прямоугольника
- area(self): метод, возвращающий площадь прямоугольника
- perimeter(self): метод, возвращающий периметр прямоугольника
- from_diagonal(cls, diagonal, aspect_ratio): класс-метод, принимающий диагональ прямоугольника и соотношение сторон и возвращающий объект класса Rectangle
- is_square(width, height): статический метод, принимающий ширину и высоту прямоугольника и возвращающий True,
если это квадрат, и False в противном случае
"""
import math


class Rectangle:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def area(self):
        return self.__width*self.__height

    def perimeter(self):
        return (self.__width+self.__height)*2

    @classmethod
    def from_diagonal(cls, diagonal, aspect_ratio):
        # a**2 + b**2 = diagonal**2
        # a / b = aspect_ratio
        # b = корень( diagonal**2 / (aspect_ratio**2 + 1) )
        # a = b * aspect_ratio
        temp_b = math.sqrt(diagonal**2 / (aspect_ratio**2 + 1))
        return Rectangle(temp_b * aspect_ratio, temp_b)

    @staticmethod
    def is_square(width, height):
        return width == height

rectangle = Rectangle(4, 5)
print(rectangle.area())  # 20
print(rectangle.perimeter())  # 18

rectangle2 = Rectangle.from_diagonal(5, 2)
print(rectangle2.width)
print(rectangle2.height)
print(rectangle2.area())  # 10.0128
print(rectangle2.perimeter())  # 13.42

print(Rectangle.is_square(4, 4))  # True
print(Rectangle.is_square(4, 5))  # False
