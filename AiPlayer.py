
class Ai:

    def __init__(self):

        self.allPossibilities = {}
        self.numbers = [0,1,2,3,4,5,6,7,8,9]
        self.numberRange = len(self.numbers)
        self.createAllPossibilities(self.numbers)
        self.gameOver = False
        self.targetNumber = None

    def createAllPossibilities(self,numbers):
        for i in range(self.numberRange):
            for j in range(self.numberRange):
                for k in range(self.numberRange):
                    for l in range(self.numberRange):
                        if(i != j) and (i != k) and (i != l) and (j != k) and (j != l) and (k != l):
                            self.allPossibilities[(i,j,k,l)] = 0

        for combination in self.allPossibilities:
            self.allPossibilities[combination] = 1 / len(self.allPossibilities)
        
    def predict(self):
        
        highestScore = 0
        highest = ()
        for combination in self.allPossibilities:
            if self.allPossibilities[combination] > highestScore:
                highestScore = self.allPossibilities[combination]
                highest = combination
        return highest

    def evaluate(self,point,prediction):
        
        if point[0] == 4:
            print("*************************")
            print("YOUR NUMBER IS FOUND: ",prediction[0],prediction[1],prediction[2],prediction[3])
            print("*************************")
            self.gameOver = True
            
        self.allPossibilities[prediction] = 0
        for combination in self.allPossibilities:
            if self.giveHint(combination,prediction) != point:
                self.allPossibilities[combination] = 0
        
        
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
        
