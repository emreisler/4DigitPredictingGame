import random

class Ai:

    def __init__(self):

        self.tumOlasiliklar = {}
        self.rakamlar = [0,1,2,3,4,5,6,7,8,9]
        self.tumOlasiliklarOlustur(self.rakamlar)
        self.gameOver = False
        self.targetNumber = self.randomNumber()
        print("TARGET NUMBER : ", self.targetNumber)

    def tumOlasiliklarOlustur(self,rakamlar):
        for i in range(len(rakamlar)):
            for j in range(len(rakamlar)):
                if(i != j):
                    self.tumOlasiliklar[(i,j)] = 0

        for combination in self.tumOlasiliklar:
            self.tumOlasiliklar[combination] = 1 / len(self.tumOlasiliklar)

    def predict(self):
        highestScore = 0
        highest = ()
        for combination in self.tumOlasiliklar:
            if self.tumOlasiliklar[combination] > highestScore:
                highestScore = self.tumOlasiliklar[combination]
                highest = combination

        return highest

    def evaluate(self,puan,prediction):

        if puan == 0:
            self.tumOlasiliklar[prediction] = 0
            self.updateScores(puan, prediction)
        if puan == 1:
            self.tumOlasiliklar[prediction] = 0
            self.updateScores(puan,prediction)
        if puan == 2:
            self.tumOlasiliklar[prediction] = 1
            self.gameOver = True
            print("NUMBER FOUND")

    def normalize(self):
        total = 0
        for combination in self.tumOlasiliklar:
            total += self.tumOlasiliklar[combination]

        for combination in self.tumOlasiliklar:
            self.tumOlasiliklar[combination]  = self.tumOlasiliklar[combination] / total
        print(self.tumOlasiliklar)


    def updateScores(self,puan,prediction):

        if puan == 0:
            for combination in self.tumOlasiliklar:
                if prediction[0] in combination or prediction[1] in combination:
                    self.tumOlasiliklar[combination] = 0

        if puan == 1:
            for combination in self.tumOlasiliklar:
                if prediction[0] in combination:
                    self.tumOlasiliklar[combination] *= puan * 2
                if prediction[1] in combination:
                    self.tumOlasiliklar[combination] *= puan * 2

    def print(self):
        print(self.tumOlasiliklar)

    def giveHint(self,prediction):

        if prediction[0] in self.targetNumber and prediction[1] in self.targetNumber:
            print("GAME OVER")
            return 2

        if prediction[0] in self.targetNumber or prediction[1] in self.targetNumber:
            return 1

        if prediction[0] not in self.targetNumber or prediction[1] not in self.targetNumber:
            return 0

    def randomNumber(self):
        number1 = random.randint(0,9)
        number2 = random.randint(0,9)
        while number2 == number1:
            number2 = random.randint(0,9)
        return number1,number2