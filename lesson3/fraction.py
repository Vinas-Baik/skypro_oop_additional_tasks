"""
Напишите класс Fraction, представляющий собой дробь, имеющий следующие методы:

- __init__(self, numerator, denominator): конструктор, принимающий числитель и знаменатель дроби;
- __repr__(self): магический метод, возвращающий строковое представление дроби,
которое можно использовать для создания нового объекта класса Fraction;
- __str__(self): магический метод, возвращающий строковое представление дроби;
- __add__(self, other): магический метод, который позволяет складывать дроби и возвращать новую дробь.
"""
import fractions
# Источник: https://pythonim.ru/chisla/klass-fraction-v-python

class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return f'{self.__class__.__name__}({self.numerator}, {self.denominator})'

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other: 'Fraction'):
        temp_st = fractions.Fraction((self.numerator*other.denominator + self.denominator*other.numerator) / (self.denominator*other.denominator))
        # Источник: https://pythonim.ru/chisla/klass-fraction-v-python
        return Fraction(temp_st.numerator, temp_st.denominator)



fraction1 = Fraction(1, 2)
print(repr(fraction1))  # Fraction(1, 2)
print(str(fraction1))  # 1/2

fraction2 = Fraction(3, 4)
print(repr(fraction2))
print(str(fraction2))
fraction3 = fraction1 + fraction2
print(fraction3)  # 5/4
