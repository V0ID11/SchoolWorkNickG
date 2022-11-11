class Board:
    def __init__(self) -> None:
        self.grid = [[" "," "," "] for i in range(3)]

    def displayBoard(self):
        print(f"   0   1   2")
        for i in range(2):
            print(f"{i}   {self.grid[i][0]} | {self.grid[i][1]} | {self.grid[i][2]}")
            print("   --------")
        print(f"{2}   {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]}")
    
    def updateBoard(self, x, y,marker):
        self.grid[y][x] = marker

    def checkSquare(self,x,y):
        if self.grid[y][x] == "":
            return True
        else:      
            return False

    def checkForWin(self):
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != " ":
                return f"{self.grid[i][0]}"

class Player:
    def __init__(self) -> None:
        pass

class Game:
    def __init__(self,numPlayers):
        self.board = Board()
        if numPlayers == 1:
            Player()
        elif numPlayers == 2:
            self.x = Player()
            self.y = Player()



game = Board()
game.displayBoard()