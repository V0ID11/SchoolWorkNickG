
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*self.width + 2* self.height

    def get_diagonal(self):
        return (self.width**2 + self.height ** 2)**0.5

height = input("Enter Height: ")
width = input("Enter Width: ")

myRect = Rectangle(float(width), float(height))
print("Area: ",round(myRect.get_area(),2))
print("Perimeter: ",round(myRect.get_perimeter(),2))
print("Diagonal Length: ",round(myRect.get_diagonal(),2))