from tkinter import *
from tkinter import font
from winsound import *
from Card import *
from Player import *
import random
theNumberOfPlayer = 3
#노 메이드 VS 노 메이드 == 무승부
class Dori:
    def __init__(self):
        self.window = Tk()
        self.window.title("Dorizikko Thang!")
        self.window.geometry("1280x760+0+0")
        self.window.configure(bg="green")

        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')

        self.cardDeck = [i for i in range(40)]
        random.shuffle(self.cardDeck)

        self.players = []
        for i in range(theNumberOfPlayer): self.players.append(Player(str(i)))
        self.dealer = Player("dealer")

        self.totalBetMoney = self.players[0].getBetMoney()+self.players[1].getBetMoney()+self.players[2].getBetMoney()
        self.playersMoney = 1000

        self.LcardsPlayers = []
        for i in range(theNumberOfPlayer): self.LcardsPlayers.append([])
        self.LcardsDealer = []

        self.deckN = 0
        self.turn = 0

        self.dealerCardsImageList = []

        self.setupLabel()
        self.setupButton()

        self.window.mainloop()

    def setupButton(self):
        self.B5P1 = Button(self.window, text="5만", width=6, height=1, font=self.fontstyle2, \
                         command=lambda X=5: self.pressedP1(X))
        self.B5P1.place(x=150, y=700)
        self.B1P1 = Button(self.window, text="1만", width=6, height=1, font=self.fontstyle2, \
                         command=lambda X=1: self.pressedP1(X))
        self.B1P1.place(x=250, y=700)

        self.B5P2 = Button(self.window, text="5만", width=6, height=1, font=self.fontstyle2, \
                         command=lambda X=5: self.pressedP2(X))
        self.B5P2.place(x=450, y=700)
        self.B1P2 = Button(self.window, text="1만", width=6, height=1, font=self.fontstyle2, \
                         command=lambda X=1: self.pressedP2(X))
        self.B1P2.place(x=550, y=700)

        self.B5P3 = Button(self.window, text="5만", width=6, height=1, font=self.fontstyle2, \
                         command=lambda X=5: self.pressedP3(X))
        self.B5P3.place(x=750, y=700)
        self.B1P3 = Button(self.window, text="1만", width=6, height=1, font=self.fontstyle2, \
                         command=lambda X=1: self.pressedP3(X))
        self.B1P3.place(x=850, y=700)

        self.Deal = Button(self.window, text="Deal", width=6, height=1, font=self.fontstyle2, command=self.pressedDeal)
        self.Deal.place(x=1050, y=700)
        self.Again = Button(self.window, text="Again", width=6, height=1, font=self.fontstyle2,
                            command=self.pressedAgain)
        self.Again.place(x=1150, y=700)

        self.B1P1["state"] = "disabled"
        self.B1P1["bg"] = "gray"
        self.B5P1["state"] = "disabled"
        self.B5P1["bg"] = "gray"
        self.B1P2["state"] = "disabled"
        self.B1P2["bg"] = "gray"
        self.B5P2["state"] = "disabled"
        self.B5P2["bg"] = "gray"
        self.B1P3["state"] = "disabled"
        self.B1P3["bg"] = "gray"
        self.B5P3["state"] = "disabled"
        self.B5P3["bg"] = "gray"

        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def initScoreLabel(self):
        self.LplayersScoreList = []
        for i in range(theNumberOfPlayer):
            tmp = []
            for j in range(5):
                label = Label(text="", width=3, height=1, font=self.fontstyle2, bg="green", fg="white")
                label.place(x=140+40*j+300*i, y=475)
                tmp.append(label)
            self.LplayersScoreList.append(tmp)

        self.LdealerScoreList = []
        for i in range(5):
            label = Label(text="", width=3, height=1, font=self.fontstyle2, bg="green", fg="white")
            label.place(x=440+40*i, y=145)
            self.LdealerScoreList.append(label)

    def setupLabel(self):
        self.LbetMoneyP1 = Label(text=str(self.players[0].getBetMoney()) + "만", width=4, height=1, font=self.fontstyle, bg="green", fg="yellow")
        self.LbetMoneyP1.place(x=200, y=650)
        self.LbetMoneyP2 = Label(text=str(self.players[1].getBetMoney()) + "만", width=4, height=1, font=self.fontstyle, bg="green", fg="yellow")
        self.LbetMoneyP2.place(x=500, y=650)
        self.LbetMoneyP3 = Label(text=str(self.players[2].getBetMoney()) + "만", width=4, height=1, font=self.fontstyle, bg="green", fg="yellow")
        self.LbetMoneyP3.place(x=800, y=650)

        self.LplayersMoney = Label(text=str(self.playersMoney - self.totalBetMoney) + "만", width=15, height=1, \
                                   font=self.fontstyle, bg="green", fg="yellow")
        self.LplayersMoney.place(x=1000, y=650)

        self.Lplayer1Status = Label(text="", width=20, height=1, font=self.fontstyle2, bg="green", fg="cyan")
        self.Lplayer1Status.place(x=150, y=445)
        self.Lplayer2Status = Label(text="", width=20, height=1, font=self.fontstyle2, bg="green", fg="cyan")
        self.Lplayer2Status.place(x=450, y=445)
        self.Lplayer3Status = Label(text="", width=20, height=1, font=self.fontstyle2, bg="green", fg="cyan")
        self.Lplayer3Status.place(x=750, y=445)

        self.LdealerStatus = Label(text="", width=20, height=1, font=self.fontstyle2, bg="green", fg="cyan")
        self.LdealerStatus.place(x=450, y=115)

        self.Lplayer1Result = Label(text="", width=10, height=1, font=self.fontstyle2, bg="green", fg="red")
        self.Lplayer1Result.place(x=200, y=350)
        self.Lplayer2Result = Label(text="", width=10, height=1, font=self.fontstyle2, bg="green", fg="red")
        self.Lplayer2Result.place(x=500, y=350)
        self.Lplayer3Result = Label(text="", width=10, height=1, font=self.fontstyle2, bg="green", fg="red")
        self.Lplayer3Result.place(x=800, y=350)

        self.initScoreLabel()

    def pressedP1(self, X):
        self.players[0].setBetMoney(self.players[0].getBetMoney()+X)
        self.LbetMoneyP1.configure(text=str(self.players[0].getBetMoney()) + "만")
        self.totalBetMoney = self.players[0].getBetMoney() + self.players[1].getBetMoney() + self.players[2].getBetMoney()
        self.LplayersMoney.configure(text=str(self.playersMoney - self.totalBetMoney) + "만")
        PlaySound('sounds/chip.wav', SND_FILENAME)
        if self.Deal["state"] == "disabled":
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"

    def pressedP2(self, X):
        self.players[1].setBetMoney(self.players[1].getBetMoney()+X)
        self.LbetMoneyP2.configure(text=str(self.players[1].getBetMoney()) + "만")
        self.totalBetMoney = self.players[0].getBetMoney() + self.players[1].getBetMoney() + self.players[2].getBetMoney()
        self.LplayersMoney.configure(text=str(self.playersMoney - self.totalBetMoney) + "만")
        PlaySound('sounds/chip.wav', SND_FILENAME)
        if self.Deal["state"] == "disabled":
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"

    def pressedP3(self, X):
        self.players[2].setBetMoney(self.players[2].getBetMoney()+X)
        self.LbetMoneyP3.configure(text=str(self.players[2].getBetMoney()) + "만")
        self.totalBetMoney = self.players[0].getBetMoney() + self.players[1].getBetMoney() + self.players[2].getBetMoney()
        self.LplayersMoney.configure(text=str(self.playersMoney - self.totalBetMoney) + "만")
        PlaySound('sounds/chip.wav', SND_FILENAME)
        if self.Deal["state"] == "disabled":
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"

    def findMade(self, tmpMonth):
        if 1 in tmpMonth:
            if 2 in tmpMonth and 7 in tmpMonth:
                return "삐리칠(1 2 7)"
            if 3 in tmpMonth and 6 in tmpMonth:
                return "물삼육(1 3 6)"
            if 4 in tmpMonth and 5 in tmpMonth:
                return "빽새오(1 4 5)"
            if 9 in tmpMonth and 10 in tmpMonth:
                return "삥구장(1 9 10)"
            tmpMonth.remove(1)
            if 1 in tmpMonth and 8 in tmpMonth:
                return "콩콩팔(1 1 8)"
            tmpMonth.append(1)
        if 2 in tmpMonth:
            if 3 in tmpMonth and 5 in tmpMonth:
                return "이삼오(2 3 5)"
            if 8 in tmpMonth and 10 in tmpMonth:
                return "이판장(2 8 10)"
            tmpMonth.remove(2)
            if 2 in tmpMonth and 6 in tmpMonth:
                return "니니육(2 2 6)"
            tmpMonth.append(2)
        if 3 in tmpMonth:
            if 7 in tmpMonth and 10 in tmpMonth:
                return "삼칠장(3 7 10)"
            if 8 in tmpMonth and 9 in tmpMonth:
                return "삼빡구(3 8 9)"
            tmpMonth.remove(3)
            if 3 in tmpMonth and 4 in tmpMonth:
                return "심심새(3 3 4)"
            tmpMonth.append(3)
        if 4 in tmpMonth:
            if 6 in tmpMonth and 10 in tmpMonth:
                return "사륙장(4 6 10)"
            if 7 in tmpMonth and 9 in tmpMonth:
                return "사칠구(4 7 9)"
            tmpMonth.remove(4)
            if 4 in tmpMonth and 2 in tmpMonth:
                return "살살이(4 4 2)"
            tmpMonth.append(4)
        if 5 in tmpMonth:
            if 6 in tmpMonth and 9 in tmpMonth:
                return "오륙구(5 6 9)"
            if 7 in tmpMonth and 8 in tmpMonth:
                return "오리발(5 7 8)"
            tmpMonth.remove(5)
            if 5 in tmpMonth and 10 in tmpMonth:
                return "꼬꼬장(5 5 10)"
            tmpMonth.append(5)
        if 6 in tmpMonth:
            tmpMonth.remove(6)
            if 6 in tmpMonth and 8 in tmpMonth:
                return "쭉쭉팔(6 6 8)"
            tmpMonth.append(6)
        if 7 in tmpMonth:
            tmpMonth.remove(7)
            if 7 in tmpMonth and 6 in tmpMonth:
                return "철철육(7 7 6)"
            tmpMonth.append(7)
        if 8 in tmpMonth:
            tmpMonth.remove(8)
            if 8 in tmpMonth and 4 in tmpMonth:
                return "팍팍싸(8 8 4)"
            tmpMonth.append(8)
        if 9 in tmpMonth:
            tmpMonth.remove(9)
            if 9 in tmpMonth and 2 in tmpMonth:
                return "구구리(9 9 2)"
            tmpMonth.append(9)
        return "노 메이드"

    def findEndNumber(self, tmp, tmpMonth, p):
        a, b, c = 0, 0, 0
        if tmp == "삐리칠(1 2 7)": a, b, c = 1, 2, 7
        elif tmp == "물삼육(1 3 6)": a, b, c = 1, 3, 6
        elif tmp == "빽새오(1 4 5)": a, b, c = 1, 4, 5
        elif tmp == "삥구장(1 9 10)": a, b, c = 1, 9, 10
        elif tmp == "콩콩팔(1 1 8)": a, b, c = 1, 1, 8
        elif tmp == "이삼오(2 3 5)": a, b, c = 2, 3, 5
        elif tmp == "이판장(2 8 10)": a, b, c = 2, 8, 10
        elif tmp == "니니육(2 2 6)": a, b, c = 2, 2, 6
        elif tmp == "삼칠장(3 7 10)": a, b, c = 3, 7, 10
        elif tmp == "삼빡구(3 8 9)": a, b, c = 3, 8, 9
        elif tmp == "심심새(3 3 4)": a, b, c = 3, 3, 4
        elif tmp == "사륙장(4 6 10)": a, b, c = 4, 6, 10
        elif tmp == "사칠구(4 7 9)": a, b, c = 4, 7, 9
        elif tmp == "살살이(4 4 2)": a, b, c = 4, 4, 2
        elif tmp == "오륙구(5 6 9)": a, b, c = 5, 6, 9
        elif tmp == "오리발(5 7 8)": a, b, c = 5, 7, 8
        elif tmp == "꼬꼬장(5 5 10)": a, b, c = 5, 5, 10
        elif tmp == "쭉쭉팔(6 6 8)": a, b, c = 6, 6, 8
        elif tmp == "철철육(7 7 6)": a, b, c = 7, 7, 6
        elif tmp == "팍팍싸(8 8 4)": a, b, c = 8, 8, 4
        else: a, b, c = 9, 9, 2
        #print("제거 전: ", tmpMonth)
        if a in tmpMonth: tmpMonth.remove(a)
        if b in tmpMonth: tmpMonth.remove(b)
        if c in tmpMonth: tmpMonth.remove(c)
        #print("제거 후: ", tmpMonth, "\n")
        for e in tmpMonth: p.setYellow(str(e))

        end = sum(tmpMonth) % 10
        if end != 0:
            p.setResult(3)
            p.setResult(end)
            return tmp + " "+str(end)+"끗"
        else:
            p.setResult(4)
            return tmp + " 망통"

    def findJokboes(self, p):
        tmpC = p.getCards()
        tmpMonth = []
        tmpNumber = []
        for c in tmpC:
            tmpMonth.append(c.getMonth())
            tmpNumber.append(c.getNumber())

        for i in range(5):
            if tmpMonth[i] == 3 and tmpNumber[i] == 1:
                for j in range(5):
                    if tmpMonth[j] == 8 and tmpNumber[j] == 1:
                        tmpMonth.remove(3)
                        tmpMonth.remove(8)
                        tmp = self.findMade(tmpMonth)
                        tmpMonth.append(3)
                        tmpMonth.append(8)
                        if tmp != "노 메이드":
                            p.setYellow(str(3))
                            p.setYellow(str(8))
                            p.setResult(0)
                            return tmp+" 38광땡"
        for i in range(5):
            if tmpMonth[i] == 1 and tmpNumber[i] == 1:
                for j in range(5):
                    if tmpMonth[j] == 8 and tmpNumber[j] == 1:
                        tmpMonth.remove(1)
                        tmpMonth.remove(8)
                        tmp = self.findMade(tmpMonth)
                        tmpMonth.append(1)
                        tmpMonth.append(8)
                        if tmp != "노 메이드":
                            p.setYellow(str(1))
                            p.setYellow(str(8))
                            p.setResult(1)
                            return tmp+" 광땡(1 8)"
                    if tmpMonth[j] == 3 and tmpNumber[j] == 1:
                        tmpMonth.remove(1)
                        tmpMonth.remove(3)
                        tmp = self.findMade(tmpMonth)
                        tmpMonth.append(1)
                        tmpMonth.append(3)
                        if tmp != "노 메이드":
                            p.setYellow(str(1))
                            p.setYellow(str(3))
                            p.setResult(1)
                            return tmp+" 광땡(1 3)"
        for i in range(1, 11):
            if i in tmpMonth:
                tmpMonth.remove(i)
                if i in tmpMonth:
                    tmpMonth.remove(i)
                    tmp = self.findMade(tmpMonth)
                    tmpMonth.append(i)
                    if tmp != "노 메이드":
                        tmpMonth.append(i)
                        p.setYellow(str(i))
                        p.setYellow(str(i))
                        p.setResult(2)
                        if i == 1:
                            p.setResult(1)
                            return tmp + " 삥땡"
                        if i == 10:
                            p.setResult(10)
                            return tmp + " 장땡"
                        else:
                            p.setResult(i)
                            return tmp + " " + str(i) + "땡"
                    else: tmpMonth.append(i)
                else: tmpMonth.append(i)

        tmp = self.findMade(tmpMonth)
        if tmp == "노 메이드": return tmp
        else: return self.findEndNumber(tmp, tmpMonth, p)

    def performance(self):
        for i in range(theNumberOfPlayer):
            tmpYellow = self.players[i].getYellow()
            if len(tmpYellow) != 0:
                for e in self.LplayersScoreList[i]:
                        if e["text"] == tmpYellow[0]:
                            e["fg"] = "yellow"
                            break
                for e in self.LplayersScoreList[i]:
                        if e["text"] == tmpYellow[1] and e["fg"] != "yellow":
                            e["fg"] = "yellow"
                            break

        tmpYellow = self.dealer.getYellow()
        if len(tmpYellow) != 0:
            for e in self.LdealerScoreList:
                if e["text"] == tmpYellow[0]:
                    e["fg"] = "yellow"
                    break
            for e in self.LdealerScoreList:
                if e["text"] == tmpYellow[1] and e["fg"] != "yellow":
                    e["fg"] = "yellow"
                    break

    def moneyCalc(self):
        vic = False
        money1, money2, money3 = 0, 0, 0
        #print(self.dealer.getResult(), self.players[0].getResult(), self.players[1].getResult(), self.players[2].getResult())
        if len(self.dealer.getResult()) != 0:

            if len(self.players[0].getResult()) != 0:

                if self.dealer.getResult()[0] > self.players[0].getResult()[0]:
                    vic = True
                    self.Lplayer1Result.configure(text="승")
                    money1 = 2 * self.players[0].getBetMoney()
                elif self.dealer.getResult()[0] < self.players[0].getResult()[0]:
                    self.Lplayer1Result.configure(text="패")
                    money1 = 0
                else:
                    if self.dealer.getResult()[1] < self.players[0].getResult()[1]:
                        vic = True
                        self.Lplayer1Result.configure(text="승")
                        money1 = 2 * self.players[0].getBetMoney()
                    elif self.dealer.getResult()[1] > self.players[0].getResult()[1]:
                        self.Lplayer1Result.configure(text="패")
                        money1 = 0
                    else:
                        self.Lplayer1Result.configure(text="무")
                        money1 = self.players[0].getBetMoney()
            else:
                self.Lplayer1Result.configure(text="패")
                money1 = 0

            if len(self.players[1].getResult()) != 0:

                if self.dealer.getResult()[0] > self.players[1].getResult()[0]:
                    vic = True
                    self.Lplayer2Result.configure(text="승")
                    money2 = 2 * self.players[1].getBetMoney()
                elif self.dealer.getResult()[0] < self.players[1].getResult()[0]:
                    self.Lplayer2Result.configure(text="패")
                    money2 = 0
                else:
                    if self.dealer.getResult()[1] < self.players[1].getResult()[1]:
                        vic = True
                        self.Lplayer2Result.configure(text="승")
                        money2 = 2 * self.players[1].getBetMoney()
                    elif self.dealer.getResult()[1] > self.players[1].getResult()[1]:
                        self.Lplayer2Result.configure(text="패")
                        money2 = 0
                    else:
                        self.Lplayer2Result.configure(text="무")
                        money2 = self.players[1].getBetMoney()
            else:
                self.Lplayer2Result.configure(text="패")
                money2 = 0

            if len(self.players[2].getResult()) != 0:

                if self.dealer.getResult()[0] > self.players[2].getResult()[0]:
                    vic = True
                    self.Lplayer3Result.configure(text="승")
                    money3 = 2 * self.players[2].getBetMoney()
                elif self.dealer.getResult()[0] < self.players[2].getResult()[0]:
                    self.Lplayer3Result.configure(text="패")
                    money3 = 0
                else:
                    if self.dealer.getResult()[1] < self.players[2].getResult()[1]:
                        vic = True
                        self.Lplayer3Result.configure(text="승")
                        money3 = 2 * self.players[2].getBetMoney()
                    elif self.dealer.getResult()[1] > self.players[2].getResult()[1]:
                        self.Lplayer3Result.configure(text="패")
                        money3 = 0
                    else:
                        self.Lplayer3Result.configure(text="무")
                        money3 = self.players[2].getBetMoney()
            else:
                self.Lplayer3Result.configure(text="패")
                money3 = 0

        else:
            if len(self.players[0].getResult()) != 0:
                vic = True
                self.Lplayer1Result.configure(text="승")
                money1 = 2 * self.players[0].getBetMoney()
            else:
                self.Lplayer1Result.configure(text="무")
                money1 = self.players[0].getBetMoney()

            if len(self.players[1].getResult()) != 0:
                vic = True
                self.Lplayer2Result.configure(text="승")
                money2 = 2 * self.players[1].getBetMoney()
            else:
                self.Lplayer2Result.configure(text="무")
                money2 = self.players[1].getBetMoney()

            if len(self.players[2].getResult()) != 0:
                vic = True
                self.Lplayer3Result.configure(text="승")
                money3 = 2 * self.players[2].getBetMoney()
            else:
                self.Lplayer3Result.configure(text="무")
                money3 = self.players[2].getBetMoney()

        tmpMoney = self.playersMoney + money1 + money2 + money3 - self.totalBetMoney
        self.playersMoney = tmpMoney
        self.LplayersMoney.configure(text=str(self.playersMoney))

        if vic: PlaySound('sounds/win.wav', SND_FILENAME)
        else: PlaySound('sounds/wrong.wav', SND_FILENAME)

    def showResult(self):
        self.B1P1["state"] = "disabled"
        self.B1P1["bg"] = "gray"
        self.B5P1["state"] = "disabled"
        self.B5P1["bg"] = "gray"
        self.B1P2["state"] = "disabled"
        self.B1P2["bg"] = "gray"
        self.B5P2["state"] = "disabled"
        self.B5P2["bg"] = "gray"
        self.B1P3["state"] = "disabled"
        self.B1P3["bg"] = "gray"
        self.B5P3["state"] = "disabled"
        self.B5P3["bg"] = "gray"

        for i in range(5):
            self.LdealerScoreList[i]["fg"] = "white"
            p = PhotoImage(file=self.dealerCardsImageList[i])
            self.LcardsDealer[i].configure(image=p)
            self.LcardsDealer[i].image = p

        self.Lplayer1Status.configure(text=self.findJokboes(self.players[0]))
        self.Lplayer2Status.configure(text=self.findJokboes(self.players[1]))
        self.Lplayer3Status.configure(text=self.findJokboes(self.players[2]))
        self.LdealerStatus.configure(text=self.findJokboes(self.dealer))

        self.performance()
        self.moneyCalc()

        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'

    def pressedDeal(self):
        if self.turn == 0:
            self.B1P1["state"] = "active"
            self.B1P1["bg"] = "white"
            self.B5P1["state"] = "active"
            self.B5P1["bg"] = "white"
            self.B1P2["state"] = "active"
            self.B1P2["bg"] = "white"
            self.B5P2["state"] = "active"
            self.B5P2["bg"] = "white"
            self.B1P3["state"] = "active"
            self.B1P3["bg"] = "white"
            self.B5P3["state"] = "active"
            self.B5P3["bg"] = "white"

            self.hitDealerDown()
            self.hitPlayers()
            PlaySound('sounds/cardFlip1.wav', SND_FILENAME)
        elif self.turn == 1:
            PlaySound('sounds/cardFlip1.wav', SND_FILENAME)
            for i in range(3):
                self.hitDealerDown()
                self.hitPlayers()
        else:
            self.hitDealerDown()
            self.hitPlayers()

            self.showResult()
        self.Deal["state"] = "disabled"
        self.Deal["bg"] = "gray"
        self.turn += 1

    def hitPlayers(self):
        for i in range(theNumberOfPlayer):
            newCard = Card(self.cardDeck[self.deckN])
            self.players[i].addCard(newCard)
            p = PhotoImage(file="GodoriCards/" + newCard.filename())
            self.LcardsPlayers[i].append(Label(self.window, image=p))
            self.LcardsPlayers[i][self.players[i].inHand() - 1].image = p
            x = 300 * i
            self.LcardsPlayers[i][self.players[i].inHand() - 1].place(x=150 + (self.players[i].inHand()-1) * 40 + x, y=530)

            self.LplayersScoreList[i][self.deckN // 4].configure(text=str(newCard.getMonth()))
            self.deckN += 1

    def hitDealerDown(self):
        newCard = Card(self.cardDeck[self.deckN])
        self.dealer.addCard(newCard)
        self.dealerCardsImageList.append("GodoriCards/" + newCard.filename())
        p = PhotoImage(file="GodoriCards/cardback.gif")
        self.LcardsDealer.append(Label(self.window, image=p))
        self.LcardsDealer[self.dealer.inHand() - 1].image = p
        self.LcardsDealer[self.dealer.inHand() - 1].place(x=450 + (self.dealer.inHand()-1) * 40, y=200)

        self.LdealerScoreList[self.deckN // 4].configure(text=str(newCard.getMonth()))
        self.LdealerScoreList[self.deckN // 4]["fg"] = "green"
        self.deckN += 1

    def pressedAgain(self):
        self.Deal["state"] = "active"
        self.Deal["bg"] = "white"

        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

        random.shuffle(self.cardDeck)
        self.deckN = 0
        self.turn = 0

        for p in self.players: p.reset()
        self.dealer.reset()

        for p in self.LcardsPlayers:
            for l in p: l.destroy()
        for l in self.LcardsDealer: l.destroy()

        self.LcardsPlayers = []
        for i in range(theNumberOfPlayer): self.LcardsPlayers.append([])
        self.LcardsDealer = []

        self.LbetMoneyP1.configure(text=str(self.players[0].getBetMoney()) + "만")
        self.LbetMoneyP2.configure(text=str(self.players[1].getBetMoney()) + "만")
        self.LbetMoneyP3.configure(text=str(self.players[2].getBetMoney()) + "만")

        for l in self.LdealerScoreList:
            l.configure(text="")
            l["fg"] = "white"
        for p in self.LplayersScoreList:
            for l in p:
                l.configure(text="")
                l["fg"] = "white"

        self.LdealerStatus.configure(text="")
        self.Lplayer1Status.configure(text="")
        self.Lplayer2Status.configure(text="")
        self.Lplayer3Status.configure(text="")

        self.Lplayer1Result.configure(text="")
        self.Lplayer2Result.configure(text="")
        self.Lplayer3Result.configure(text="")

        self.dealerCardsImageList = []

        PlaySound('sounds/ding.wav', SND_FILENAME)

Dori()