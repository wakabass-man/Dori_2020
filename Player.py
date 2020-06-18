class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.N = 0 #카드 갯수
        self.betMoney = 0
        self.yellow = []
        self.result = []
    def addCard(self, c):
        self.cards.append(c)
        self.N += 1
    def inHand(self):
        return self.N
    def reset(self):
        self.N = 0
        self.cards.clear()
        self.betMoney = 0
        self.yellow.clear()
        self.result.clear()
    def getResult(self):
        return self.result
    def setResult(self, n):
        self.result.append(n)
    def getYellow(self):
        return self.yellow
    def setYellow(self, n):
        self.yellow.append(n)
    def getCards(self):
        return self.cards
    def setBetMoney(self, m):
        self.betMoney = m
    def getBetMoney(self):
        return self.betMoney