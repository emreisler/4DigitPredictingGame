from AiPlayer import Ai

def main():
    '''
    Error states are not implemented just because.
    '''
    move = 0 # initilize move counter
    aiPlayer = Ai() # create aiPlayer object
    human_number = input("Enter your number : ") # request number
    aiPlayer.targetNumber = (int(human_number[0]),int(human_number[1]),int(human_number[2]),int(human_number[3])) #take human number as tuple 
    
    while not aiPlayer.gameOver:
        move += 1
        prediction = aiPlayer.predict() # make prediction
        print("PREDICTION",move," : ",prediction[0],prediction[1],prediction[2],prediction[3])
        hint = aiPlayer.giveHint(prediction,aiPlayer.targetNumber) # calculate and give hint
        print("HINT : ", hint[0],"a ",hint[1],"b")
        aiPlayer.evaluate(hint,prediction) # evaluate the prediction per hint
        
    print("TOTAL MOVES : ", move) # print total moves
    print("GAME OVER")
    

if __name__ == '__main__':
    main()
