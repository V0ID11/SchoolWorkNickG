# Skeleton Program code for the AQA A Level Paper 1 2018 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed using Python 3.5.1

import random

class QueueOfTiles():
  def __init__(self, MaxSize,allowedWords):
    self._Contents = []
    self._Rear = -1
    self._MaxSize = MaxSize
    self.getDistribution(allowedWords)
    for Count in range(self._MaxSize):
      self._Contents.append("")
      self.Add()
    
  def IsEmpty(self):
    if self._Rear == -1:
      return True
    else:
      return False

  def Remove(self):
    if self.IsEmpty():
      return None
    else:
      Item = self._Contents[0]
      for Count in range (1, self._Rear + 1):
        self._Contents[Count - 1] = self._Contents[Count]
      self._Contents[self._Rear] = ""
      self._Rear -= 1
      return Item
  
  def getDistribution(self,allowedWords):
    self.letters = []
    for i in range(25):
      x = 0
      for y in allowedWords:
        x += y.count(chr(i+65))
      print(x)
      self.letters.append(x)
    print(self.letters)

  def Add(self):
    if self._Rear < self._MaxSize - 1:
      RandNo = random.choices([i for i in range(25)],weights=self.letters)
      self._Rear += 1
      self._Contents[self._Rear] = chr(65 + RandNo[0])

  def Show(self):
    if self._Rear != -1:
      print()
      print("The contents of the queue are: ", end="")
      for Item in self._Contents:
        print(Item, end="")
      print()

def CreateTileDictionary():
  TileDictionary = dict()
  for Count in range(26):
    if Count in [0, 4, 8, 13, 14, 17, 18, 19]:
      TileDictionary[chr(65 + Count)] = 1
    elif Count in [1, 2, 3, 6, 11, 12, 15, 20]:
      TileDictionary[chr(65 + Count)] = 2
    elif Count in [5, 7, 10, 21, 22, 24]:
      TileDictionary[chr(65 + Count)] = 3
    else:
      TileDictionary[chr(65 + Count)] = 5
  return TileDictionary
    
def DisplayTileValues(TileDictionary, AllowedWords):
  print()
  print("TILE VALUES")
  print()  
  for Letter, Points in TileDictionary.items():
    print("Points for " + Letter + ": " + str(Points))
  print()

def GetStartingHand(TileQueue, StartHandSize):
  Hand = ""
  for Count in range(StartHandSize):
    Hand += TileQueue.Remove()
    TileQueue.Add()
  return Hand

def LoadAllowedWords():
  AllowedWords = []
  try:
    WordsFile = open("aqawords.txt", "r")
    for Word in WordsFile:
      AllowedWords.append(Word.strip().upper())
    WordsFile.close()
  except:
    raise Exception("Need a file named aqawords.txt")
  return AllowedWords

def CheckWordIsInTiles(Word, PlayerTiles):
  InTiles = True
  CopyOfTiles = PlayerTiles
  for Count in range(len(Word)):
    if Word[Count] in CopyOfTiles:
      CopyOfTiles = CopyOfTiles.replace(Word[Count], "", 1)
    else:
      InTiles = False
  return InTiles 

def CheckWordIsValid(Word, AllowedWords):
  start = 0
  end = len(sorted(AllowedWords))-1
  while start <= end:
    position = (start + end)//2
    if AllowedWords[position] == Word:
      return True
    elif AllowedWords[position] > Word:
      end = position - 1
    else:
      start = position + 1
  # if found == False:
  #   if AllowedWords[end] == Word:
  #     found = True
  return False

def AddEndOfTurnTiles(TileQueue, PlayerTiles, NewTileChoice, Choice):
  if NewTileChoice == "1":
    NoOfEndOfTurnTiles = len(Choice)
  elif NewTileChoice == "2":
    NoOfEndOfTurnTiles = 3    
  else:
    NoOfEndOfTurnTiles = len(Choice) + 3
  for Count in range(NoOfEndOfTurnTiles):
    PlayerTiles += TileQueue.Remove()
    TileQueue.Add()
  return TileQueue, PlayerTiles  

def FillHandWithTiles(TileQueue, PlayerTiles, MaxHandSize):
  while len(PlayerTiles) <= MaxHandSize:
    PlayerTiles += TileQueue.Remove()
    TileQueue.Add()
  return TileQueue, PlayerTiles  

def GetScoreForWord(Word, TileDictionary):
  Score = 0
  for Count in range (len(Word)):
    Score += TileDictionary[Word[Count]]
  if len(Word) > 7:
    Score += 20
  elif len(Word) > 5:
    Score += 5
  return Score
  
def UpdateAfterAllowedWord(Word, PlayerTiles, PlayerScore, PlayerTilesPlayed, TileDictionary, AllowedWords):
  PlayerTilesPlayed += len(Word)
  for Letter in Word:
    PlayerTiles = PlayerTiles.replace(Letter, "", 1)
  PlayerScore += GetScoreForWord(Word, TileDictionary)
  return PlayerTiles, PlayerScore, PlayerTilesPlayed
      
def UpdateScoreWithPenalty(PlayerScore, PlayerTiles, TileDictionary):
  for Count in range(len(PlayerTiles)):
    PlayerScore -= TileDictionary[PlayerTiles[Count]]  
  return PlayerScore

def GetChoice():
  print()
  print("Either:")
  print("     enter the word you would like to play OR")
  print("     press 1 to display the letter values OR")
  print("     press 4 to view the tile queue OR")
  print("     press 7 to view your tiles again OR")
  print("     press 0 to fill hand and stop the game.")
  Choice = input(">")
  print()
  Choice = Choice.upper()
  return Choice

def GetNewTileChoice():
  NewTileChoice = ""
  while NewTileChoice not in ["1", "2", "3", "4"]:
    print("Do you want to:")
    print("     replace the tiles you used (1) OR")
    print("     get three extra tiles (2) OR")
    print("     replace the tiles you used and get three extra tiles (3) OR")
    print("     get no new tiles (4)?")
    NewTileChoice = input(">")
  return NewTileChoice

def DisplayTilesInHand(PlayerTiles):
  print()
  print("Your current hand:", PlayerTiles)
  
def HaveTurn(PlayerName, PlayerTiles, PlayerTilesPlayed, PlayerScore, TileDictionary, TileQueue, AllowedWords, MaxHandSize, NoOfEndOfTurnTiles):
  print()
  print(PlayerName, "it is your turn.")
  DisplayTilesInHand(PlayerTiles)
  NewTileChoice = "2"
  ValidChoice = False
  while not ValidChoice:
    Choice = GetChoice()
    if Choice == "1":
      DisplayTileValues(TileDictionary, AllowedWords)
    elif Choice == "4":
      TileQueue.Show()
    elif Choice == "7":
      DisplayTilesInHand(PlayerTiles)      
    elif Choice == "0":
      ValidChoice = True
      TileQueue, PlayerTiles = FillHandWithTiles(TileQueue, PlayerTiles, MaxHandSize)
    else:
      ValidChoice = True
      if len(Choice) == 0:
        ValidWord = False
      else:
        ValidWord = CheckWordIsInTiles(Choice, PlayerTiles)
      if ValidWord:
        ValidWord = CheckWordIsValid(Choice, AllowedWords)
        if ValidWord:
          print()
          print("Valid word")
          print()
          PlayerTiles, PlayerScore, PlayerTilesPlayed = UpdateAfterAllowedWord(Choice, PlayerTiles, PlayerScore, PlayerTilesPlayed, TileDictionary, AllowedWords)
          NewTileChoice = GetNewTileChoice()
      if not ValidWord:
        print()
        print("Not a valid attempt, you lose your turn.")
        print()
      if NewTileChoice != "4":
        TileQueue, PlayerTiles = AddEndOfTurnTiles(TileQueue, PlayerTiles, NewTileChoice, Choice)
      print()
      print("Your word was:", Choice)
      print("Your new score is:", PlayerScore)
      print("You have played", PlayerTilesPlayed, "tiles so far in this game.")
  return PlayerTiles, PlayerTilesPlayed, PlayerScore, TileQueue  

def DisplayWinner(playerOneName,playerTwoName,PlayerOneScore, PlayerTwoScore):
  print()
  print("**** GAME OVER! ****")
  print()
  print(f"{playerOneName} your score is", PlayerOneScore)
  print(f"{playerTwoName} your score is", PlayerTwoScore)
  if PlayerOneScore > PlayerTwoScore:
    with open("highscore.txt","r+") as f:
      highscore = f.readline()
      if PlayerOneScore > int(highscore):
        f.writelines(str(PlayerOneScore))
      
    print(f"{playerOneName} wins!")
  elif PlayerTwoScore > PlayerOneScore:
    with open("highscore.txt","r+") as f:
      highscore = f.readline()
      if PlayerTwoScore > int(highscore):
        f.writelines(str(PlayerTwoScore))
    print(f"{playerTwoName} wins!")
  else:
    print("It is a draw!")
  print()
  
def PlayGame(AllowedWords, TileDictionary, RandomStart, StartHandSize, MaxHandSize, MaxTilesPlayed, NoOfEndOfTurnTiles):
  PlayerOneScore = 50
  PlayerTwoScore = 50
  PlayerOneTilesPlayed = 0
  PlayerTwoTilesPlayed = 0
  TileQueue = QueueOfTiles(20,AllowedWords)
  PlayerOneName = input("What is the Name of the first player? ")
  playerTwoName = input("What is the Name of the second Player?")
  if RandomStart:
    PlayerOneTiles = GetStartingHand(TileQueue, StartHandSize)
    PlayerTwoTiles = GetStartingHand(TileQueue, StartHandSize)
  else:
    PlayerOneTiles = "BTAHANDENONSARJ"
    PlayerTwoTiles = "CELZXIOTNESMUAA"
  while PlayerOneTilesPlayed <= MaxTilesPlayed and PlayerTwoTilesPlayed <= MaxTilesPlayed and len(PlayerOneTiles) < MaxHandSize and len(PlayerTwoTiles) < MaxHandSize:
    PlayerOneTiles, PlayerOneTilesPlayed, PlayerOneScore, TileQueue = HaveTurn(PlayerOneName, PlayerOneTiles, PlayerOneTilesPlayed, PlayerOneScore, TileDictionary, TileQueue, AllowedWords, MaxHandSize, NoOfEndOfTurnTiles)
    print()
    input("Press Enter to continue")
    print()
    PlayerTwoTiles, PlayerTwoTilesPlayed, PlayerTwoScore, TileQueue = HaveTurn(playerTwoName, PlayerTwoTiles, PlayerTwoTilesPlayed, PlayerTwoScore, TileDictionary, TileQueue, AllowedWords, MaxHandSize, NoOfEndOfTurnTiles)
  PlayerOneScore = UpdateScoreWithPenalty(PlayerOneScore, PlayerOneTiles, TileDictionary)
  PlayerTwoScore = UpdateScoreWithPenalty(PlayerTwoScore, PlayerTwoTiles, TileDictionary)
  DisplayWinner(PlayerOneName, playerTwoName, PlayerOneScore, PlayerTwoScore)

def DisplayMenu():
  print()
  print("=========")
  print("MAIN MENU")
  print("=========")
  print()
  print("1. Play game with random start hand")
  print("2. Play game with training start hand")
  print("9. Quit")
  print()
  
def Main():
  print("++++++++++++++++++++++++++++++++++++++")
  print("+ Welcome to the WORDS WITH AQA game +")
  print("++++++++++++++++++++++++++++++++++++++")
  print()
  print()
  AllowedWords = LoadAllowedWords()
  TileDictionary = CreateTileDictionary()
  MaxHandSize = 20
  MaxTilesPlayed = 50
  NoOfEndOfTurnTiles = 3
  StartHandSize = 15
  Choice = ""
  while Choice != "9":
    DisplayMenu()
    Choice = input("Enter your choice: ")
    if Choice == "1":
      PlayGame(AllowedWords, TileDictionary, True, StartHandSize, MaxHandSize, MaxTilesPlayed, NoOfEndOfTurnTiles)
    elif Choice == "2":
      PlayGame(AllowedWords, TileDictionary, False, 15, MaxHandSize, MaxTilesPlayed, NoOfEndOfTurnTiles)
      
if __name__ == "__main__":
  Main()