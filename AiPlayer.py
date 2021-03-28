import random

class Ai:

    def __init__(self):

        self.tumOlasiliklar = {}
        self.rakamlar = [0,1,2,3,4,5,6,7,8,9]
        self.tumOlasiliklarOlustur(self.rakamlar)
        self.gameOver = False
        self.targetNumber = self.randomNumber(self.rakamlar)
        self.moveCount = 0
        self.alpha = 0.8
        self.initialRandomTrial = 7
        self.predictionHistory = []
        
        

    def tumOlasiliklarOlustur(self,rakamlar):
        for i in range(len(rakamlar)):
            for j in range(len(rakamlar)):
                for k in range(len(rakamlar)):
                    for l in range(len(rakamlar)):
                        if(i != j) and (i != k) and (i != l) and (j != k) and (j != l) and (k != l):
                            self.tumOlasiliklar[(i,j,k,l)] = 0

        for combination in self.tumOlasiliklar:
            self.tumOlasiliklar[combination] = 1 / len(self.tumOlasiliklar)
        
        
    def predict(self):
        
        highestScore = 0
        highest = ()
        for combination in self.tumOlasiliklar:
            if self.tumOlasiliklar[combination] > highestScore:
                highestScore = self.tumOlasiliklar[combination]
                highest = combination
        self.moveCount += 1
        return highest

    def evaluate(self,puan,prediction):
        
        if puan[0] == 4:
            print("*************************")
            print("YOUR NUMBER : ",prediction[0],prediction[1],prediction[2],prediction[3])
            print("*************************")
            print("GAME OVER")
            self.gameOver = True
            
        self.tumOlasiliklar[prediction] = 0
        for combination in self.tumOlasiliklar:
            if self.giveHint(combination,prediction) != puan:
                self.tumOlasiliklar[combination] = 0
        
            
    def normalize(self):
        total = 0
        for combination in self.tumOlasiliklar:
            total += self.tumOlasiliklar[combination]

        for combination in self.tumOlasiliklar:
            try:
                
                self.tumOlasiliklar[combination]  = self.tumOlasiliklar[combination] / total
            except :
                pass
        #print(self.tumOlasiliklar)


    def print(self):
        print(self.tumOlasiliklar)

    def giveHint(self,prediction,target):
        pointsA = 0
        pointsB = 0
        for i in range(4):
            if prediction[i] in target:
                if prediction[i] == target[i]:
                    pointsA += 1
                else:
                    pointsB += 1
                    
        return pointsA,pointsB
      

    def randomNumber(self,rakamlar):
        
        copyRakamlar = rakamlar.copy()
        number1 = copyRakamlar.pop(random.randint(0,9))
        number2 = copyRakamlar.pop(random.randint(0,8))
        number3 = copyRakamlar.pop(random.randint(0,7))
        number4 = copyRakamlar.pop(random.randint(0,6))
        
        
        return number1,number2,number3,number4
    
    def zeroPossibilitesList(self):
        zeroPoss = 0
        for combination in self.tumOlasiliklar:
            if self.tumOlasiliklar[combination] == 0:
                zeroPoss += 1
        
        
    
    def checkHistory(self,prediction):
        if len(self.predictionHistory) > 0:
            for combination in self.predictionHistory:
                sameNumberPredicted = 0
                for i in range(4):
                    if prediction[i] in combination:
                        sameNumberPredicted += 1
                if sameNumberPredicted > 2:
                    return False
                else:
                    return True
        else:
            return True
        
        
