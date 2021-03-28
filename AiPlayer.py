
class Ai:

    def __init__(self):
        '''
        İnitilize required fields for Ai objects.
        '''
        self.allPossibilities = {} # initilize a dict to keep all possible moves
        self.numbers = [0,1,2,3,4,5,6,7,8,9] # initilize numbers
        self.numberRange = len(self.numbers) # calculate length of numbers 
        self.createAllPossibilities(self.numbers)
        self.gameOver = False # initilize gameOver as false
        self.targetNumber = None # initilize a targetNumber field

    
    def createAllPossibilities(self,numbers):
        '''
        Creates all possibilities in dict and assign their initial rankings
        '''
        for i in range(self.numberRange):
            for j in range(self.numberRange):
                for k in range(self.numberRange):
                    for l in range(self.numberRange):
                        if(i != j) and (i != k) and (i != l) and (j != k) and (j != l) and (k != l):
                            self.allPossibilities[(i,j,k,l)] = 0
                            
        #assign initial rankings of dict elements
        for combination in self.allPossibilities:
            self.allPossibilities[combination] = 1 / len(self.allPossibilities)
        
    def predict(self):
        '''
        Makes prediction by choosing the highest rating one from all possibilities dict.
        '''
        highestScore = 0
        highest = ()
        for combination in self.allPossibilities:
            if self.allPossibilities[combination] > highestScore:
                highestScore = self.allPossibilities[combination]
                highest = combination
        return highest

    def evaluate(self,point,prediction):
        
        '''
        Evaluates the prediction per given hint
        '''
        
        # GameOver condition
        if point[0] == 4:
            print("*************************")
            print("YOUR NUMBER IS FOUND: ",prediction[0],prediction[1],prediction[2],prediction[3])
            print("*************************")
            self.gameOver = True
        
        #If game is not over than eleminate the current prediction    
        self.allPossibilities[prediction] = 0
        
        #Loop through all possible moves and if their hint for current prediction does not match with current hint, eleminate them.
        for combination in self.allPossibilities:
            if self.giveHint(combination,prediction) != point:
                self.allPossibilities[combination] = 0
        
        
    def giveHint(self,prediction,target):
        '''
        Calculates and returns hint
        '''
        pointsA = 0
        pointsB = 0
        for i in range(4):
            if prediction[i] in target:
                if prediction[i] == target[i]:
                    pointsA += 1
                else:
                    pointsB += 1
                    
        return pointsA,pointsB
    
