import random

class Board:
    def __init__(self) -> None:
        self.grid = [[" "," "," "] for i in range(3)]

    def displayBoard(self):
        print(f"    0   1   2")
        for i in range(2):
            print(f"{i}   {self.grid[i][0]} | {self.grid[i][1]} | {self.grid[i][2]}")
            print("    ---------")
        print(f"{2}   {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]}")
    
    def updateBoard(self, x, y, player):
        self.grid[y][x] = player

    def checkSquare(self,x,y):
        if self.grid[y][x] == "":
            return False
        else:      
            return True

    def checkForWin(self):
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] and self.grid[i][0] != " ":
                return True
            elif self.grid[0][i] == self.grid[1][i] == self.grid[2][i] and self.grid[0][i] != " ":
                return True
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != " " or self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[2][2]!= " ":
            return True
        else:
            return False

class Player:
    def __init__(self, name, marker) -> None:
        self.name = name
        self.marker = marker
    def __str__(self) -> str:
        return self.marker
    def __repr__(self) -> str:
        return self.name

class Game:
    def __init__(self, numPlayers):
        self.board = Board()
        if numPlayers == 1:
            p1Name = input("What is the name of Player 1")
            m1 = input("What letter does Player 1 want as marker?")
            self.player1 = Player(p1Name,m1)
            if m1.upper() == "X": 
                self.computer = Player("Computer", "O")
            else:
                self.computer = Player("Computer", "X")
        
        elif numPlayers == 2:
            p1Name = input("What is the name of Player 1")
            m1 = input("What letter does Player 1 want as marker?")
            self.player1 = Player(p1Name,m1)
            p2Name = input("What is the name of Player 1")
            m2 = input("What letter does Player 1 want as marker?")
            self.player2 = Player(p2Name,m2)
            
    def gameLoopComputer(self):
        while True:
            self.board.displayBoard()
            move = input(f"Where will {self.player1.name} go in the form x,y")
            x,y = move.split(",")
            while self.board.checkSquare(int(x), int(y)) == False:
                move = input(f"Where will {self.player1.name} go in the form x,y")
                move.split(",")
            self.board.updateBoard(int(x), int(y), self.player1)
            self.board.displayBoard()
            if self.board.checkForWin() == True:
                return  f"{self.player1.__repr__()} wins"
            self.board.displayBoard()            
            x,y = random.randint(0,3),random.randint(0,3)
            while self.board.checkSquare(int(x), int(y)) == False:
                x,y = random.randint(0,3),random.randint(0,3)
            self.board.updateBoard(x,y,self.computer)
            if self.board.checkForWin() == True:
                return  f"Computer Wins"
    def gameLoop2Player(self):
        while True:
            self.board.displayBoard()
            move = input(f"Where will {self.player1.name} go in the form x,y")
            x,y = move.split(",")
            while self.board.checkSquare(int(x), int(y)) == False:
                move = input(f"Where will {self.player1.name} go in the form x,y")
                move.split(",")
            self.board.updateBoard(int(x), int(y), self.player1)
            if self.board.checkForWin() == True:
                return  f"{self.player1.__repr__()} Wins"
            self.board.displayBoard()
            move = input(f"Where will {self.player2.name} go in the form x,y")
            x,y = move.split(",")
            while self.board.checkSquare(int(x), int(y)) == False:
                move = input(f"Where will {self.player2.name} go in the form x,y")
                move.split(",")
            self.board.updateBoard(int(x), int(y), self.player2)
            if self.board.checkForWin() == True:
                return  f"{self.player2.__repr__()} Wins"
            self.board.displayBoard()



numPlayer = int(input("How Many Players? "))
game = Game(numPlayer)
if numPlayer == 1:
    print(game.gameLoop2Player())
else:
    print(game.gameLoopComputer())
