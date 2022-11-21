import random

class Board:
    def __init__(self) -> None:
        self.grid = [[" "," "," "],[" "," "," "],[" "," "," "]]

    def displayBoard(self):
        print(f"    0   1   2")
        for i in range(2):
            print(f"{i}   {self.grid[i][0]} | {self.grid[i][1]} | {self.grid[i][2]}")
            print("    ---------")
        print(f"{2}   {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]}")
    
    def updateBoard(self, x, y, player):
        self.grid[y][x] = player

    def checkSquare(self,x,y):
        if self.grid[y][x] != " ":
            return True
        else:      
            return False

    def checkForWin(self):
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] and self.grid[i][0] != " ":
                return True
            elif self.grid[0][i] == self.grid[1][i] == self.grid[2][i] and self.grid[0][i] != " ":
                return True
        if (self.grid[0][0] == self.grid[1][1] == self.grid[2][2] or self.grid[0][2] == self.grid[1][1] == self.grid[2][0]) and self.grid[1][1]!= " ":
            return True
        else:
            return False

class Player:
    def __init__(self, name, marker) -> None:
        self.name = name
        self.marker = marker
    def __str__(self) -> str:
        return self.marker
    def get_Name(self) -> str:
        return self.name
    def get_move(self):
        raise NotImplemented

class Computer(Player):
    def __init__(self, name, marker) -> None:
        super().__init__(name, marker)

    def get_move(self):
        return f"{random.randint(0,2)}, {random.randint(0,2)}"

class Human(Player):
    def __init__(self, name, marker) -> None:
        super().__init__(name, marker)

    def get_move(self):
        move = input("Where do you want to move in the form x,y")
        return move

class Game:
    def __init__(self, numPlayers):
        self.board = Board()
        if numPlayers == 1:
            p1Name = input("What is the name of Player 1")
            m1 = input("What letter does Player 1 want as marker?")
            self.player1 = Human(p1Name,m1)
            if m1.upper() == "X": 
                self.player2 = Computer("Computer", "O")
            else:
                self.player2 = Computer("Computer", "X")
        
        elif numPlayers == 2:
            p1Name = input("What is the name of Player 1")
            m1 = input("What letter does Player 1 want as marker?")
            self.player1 = Human(p1Name,m1)
            p2Name = input("What is the name of Player 1")
            m2 = input("What letter does Player 1 want as marker?")
            self.player2 = Human(p2Name,m2)
            
    def gameLoop(self):
        while True:
            self.board.displayBoard()

            move = self.player1.get_move()
            x,y = move.split(",")
            while self.board.checkSquare(int(x), int(y)) != False:
                move = self.player1.get_move()
                x,y = move.split(",")

            self.board.updateBoard(int(x), int(y), self.player1)
            self.board.displayBoard()

            if self.board.checkForWin() == True:
                return  f"{self.player1.get_Name()} Wins"


            self.board.displayBoard()     

            move = self.player2.get_move()
            x,y = move.split(",")
            while self.board.checkSquare(int(x), int(y)) != False:
                move = self.player2.get_move()
                x,y = move.split(",")

            self.board.updateBoard(int(x),int(y),self.player2)
            if self.board.checkForWin() == True:
                return  f"{self.player2.get_Name} Wins"
    


numPlayer = int(input("How Many Players? "))
game = Game(numPlayer)
print(game.gameLoop())

