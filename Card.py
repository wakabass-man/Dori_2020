class Card:
    def __init__(self, temp):
        self.month = temp // 4 + 1
        self.number = temp % 4 + 1
    def getMonth(self):
        return self.month
    def getNumber(self):
        return self.number
    def filename(self):
        return str(self.month)+"."+str(self.number)+".gif"