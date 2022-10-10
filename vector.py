from __future__ import annotations

class Vector:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def __add__(self,other)  -> Vector:
        newX = self.x + other.x
        newY = self.y + other.y
        return Vector(newX, newY)

    def __str__(self) -> str:
        return f"[{self.x}, {self.y}]"

    def magnitude(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def unitVector(self):
        return Vector(self.x/self.magnitude(), self.y/self.magnitude())
    
    def __mul__(self,other) -> Vector:
        return Vector(self.x * other, self.y * other)
    
    def __rmul__(self,other) -> Vector:
        return Vector(self.x * other, self.y * other)

a = Vector(5,9)
print(a)
print(a.magnitude())
b = Vector(6,2)
z = a + b
print(b.unitVector())
print(z)

x = a * 8

y = 8 * Vector(3, 4)
print(x)
print(y)