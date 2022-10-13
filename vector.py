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
    
    def __eq__(self, other) -> bool:
        return True if self.x == other.x and self.y == other.y else False

def test_vector():
    vec1 = Vector(3, 4)
    vec2 = Vector(4, 5)

    # Test magnitude
    print("Testing magnitude function...", end='')
    if vec1.magnitude() == 5:
        print('Test passed')
    else:
        print('Test FAILED!')

    # Test equality
    print("Testing equality...")
    assert Vector(1, 2) == Vector(1, 2), 'Equality method not working'


    # Test Addition
    print("Testing addition...", end='')
    if vec1 + vec2 == Vector(7, 9):
        print('Test passed')
    else:
        print('Test FAILED!')
test_vector()