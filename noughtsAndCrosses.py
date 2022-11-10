class Board:
    def __init__(self) -> None:
        self.grid = [["","",""] for i in range(3)]

    def displayBoard(self):
        print(f"   0  1  2")
        for i in range(2):
            print(f"{i}   {self.grid[i][0]} | {self.grid[i][1]} | {self.grid[i][2]}")
            print("   --------")
        print(f"{2}   {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]}")
    
    def updateBoard(self, x, y,marker):
        self.grid[y][x] = marker

    def checkSquare(x,y):
        if self.grid[y][x]:
            pass

    def checkForWin():
        pass

class Player:
    def __init__(self) -> None:
        pass

game = Board()
game.updateBoard(2,1,'X')
game.displayBoard()

