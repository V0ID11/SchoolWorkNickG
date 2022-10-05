from gzip import READ
from turtle import width


class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def get_area(self):
        return round(self.width * self.height,2)
    def get_perimeter(self):
        return round(2*self.width + 2* self.height,2)
    def get_diagonal(self):
        return round((self.width**2 + self.height ** 2)**0.5,2)

height = input("Enter Height: ")
width = input("Enter Width: ")

myRect = Rectangle(float(width), float(height))
print("Area: ",myRect.get_area())
print("Perimeter: ",myRect.get_perimeter())
print("Diagonal Length: ",myRect.get_diagonal())