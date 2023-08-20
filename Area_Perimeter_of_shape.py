from abc import ABC , abstractmethod
from math import sqrt , pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self,side):
        self.__side=side

    def area(self):
        return f" Area = {round(self.__side * self.__side,2)} "

    def perimeter(self):
        return f" Perimeter = {round(self.__side * 4 ,2)} "


class Rectangle(Shape):
    def __init__(self,length,width):
        self.__length=length
        self.__width=width

    def area(self):
        return f" Area = {round(self.__length * self.__width ,2)} "

    def perimeter(self):
        return f" Perimeter = { round(2 * (self.__length + self.__width),2)} "


class Circle(Shape):
    def __init__(self,radius):
        self.__radius=radius

    def area(self):
        return f" Area = {round(pi * 2 * self.__radius,2) } "

    def perimeter(self):
        return f" Perimeter = {round(pi * self.__radius,2) } "


class Triangle(Shape):
    def __init__(self,side1,side2,side3):
        self.__side1=side1
        self.__side2=side2
        self.__side3=side3

    def area(self):
        s=( (self.__side1 + self.__side2 + self.__side3) / 2)
        return f" Area = {round(sqrt(s * (s - self.__side1) * (s - self.__side2 ) * (s - self.__side3) ),2)} "

    def perimeter(self):
        return f" Perimeter = {round((self.__side1 + self.__side2 + self.__side3),2)} "


class Equilateral_Triangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)

class Isosceles_Triangle(Triangle):
    def __init__(self, base, height):
        super().__init__(base, base, sqrt(base**2 + height**2))

class Scalene_Triangle(Triangle):
    pass



print("-------------------")
print("1- Square Calculator")
print("2- Rectangle Calculator")
print("3- Circle Calculator")
print("4- Triangle Calculator")
print("-------------------")
User_Choice=int(input("Chose a number:"))

if User_Choice == 1 :
    side_length=int(input("Enter the side length of the square:"))
    square = Square(side_length)
    print(square.area())
    print(square.perimeter())

elif User_Choice == 2 :
    length=int(input("Enter the length of the rectangle :"))
    width=int(input("Enter the width of the rectangle :"))
    rectangle = Rectangle(width,length)
    print(rectangle.area())
    print(rectangle.perimeter())

elif User_Choice == 3 :
    radius=int(input("Enter the radius of the circle :"))
    circle = Circle(radius)
    print(circle.area())
    print(circle.perimeter()) 

elif User_Choice == 4 :
    print("-------------------")
    print("1- Equilateral Triangle")
    print("2- Isosceles Triangle")
    print("3- Scalene Triangle")
    print("-------------------")
    User_Choice=int(input("Chose a number:"))

    if User_Choice == 1 :
        side=int(input("Enter the length of a side:"))   
        equilateral_triangle=Equilateral_Triangle(side)
        print(equilateral_triangle.area())
        print(equilateral_triangle.perimeter())

    elif User_Choice == 2 :
        base = int(input("Enter the length of the base: "))
        side = int(input("Enter the length of a side: "))  
        isosceles_triangle=Isosceles_Triangle(2,3)
        print(isosceles_triangle.area())
        print(isosceles_triangle.perimeter())

    elif User_Choice == 3 :
        side1 = int(input("Enter the length of the first side: "))
        side2 = int(input("Enter the length of the second side: "))
        side3 = int(input("Enter the length of the third side: "))
        scalene_triangle=Scalene_Triangle(side1,side2,side3)
        print(scalene_triangle.area())
        print(scalene_triangle.perimeter())
    else:
        print("Wrong choice!")

else:
    print("Wrong choice!")
    