

class StockItem:
    def __init__(self,Title: str, OnLoan: bool, DateAcquired:str) -> None:
        self._Title = Title
        self._OnLoan = OnLoan
        self._DateAcquired = DateAcquired
    def setLoan(self):
        if self._OnLoan == True:
            self._OnLoan = False
        else:
            self._OnLoan = True


class Book(StockItem):
    def __init__(self, Title: str, OnLoan: bool, DateAcquired: str, Author: str, ISBN: str) -> None:
        super().__init__(Title, OnLoan, DateAcquired)
        self._Author = Author
        self._ISBN = ISBN
    def displayDetails(self):
        print("Title\tAuthor\tOn Loan\tDateAcquired\tISBN")
        print(f"{self._Title}\t{self._Author}\t{self._OnLoan}\t{self._DateAcquired}\t{self._ISBN}")

class CD(StockItem):
    def __init__(self, Title: str, OnLoan: bool, DateAcquired: str, Artist: str, playTime: float) -> None:
        super().__init__(Title, OnLoan, DateAcquired)
        self._Artist = Artist
        self._playTime = playTime
    def displayDetails(self):
        print("Title\tArtist\tOn Loan\tDateAcquired\tPlaytime")
        print(f"{self._Title}\t{self._Artist}\t{self._OnLoan}\t{self._DateAcquired}\t{self._playTime}")

throne = Book("Throne Of Glass",False,"14/10/2022","Sarah J Mass","834956230")
throne.displayDetails()
throne.setLoan()
throne.displayDetails()