def getTriangulars():
     triangleList = set()
     for i in range(100000):
        triangleList.add(0.5*i*(i+1))
     return triangleList

def getPentagulars():
    pentagonalList = set()
    for i in range(100000):
        pentagonalList.add(0.5*i*(3*i-1))
    return pentagonalList

def getHexagulars():
    hexagonalList = set()
    for i in range(100000):
        hexagonalList.add(i*(2*i-1))
    return hexagonalList

def intersect(t,p,h):
    return t&(p&h)

triangulars = getTriangulars()
pentagonals = getPentagulars()
hexagonals = getHexagulars()

x = intersect(triangulars,pentagonals,hexagonals)

print(x)