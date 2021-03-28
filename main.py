from AiPlayer import Ai

def main():

    move = 0
    aiPlayer = Ai()
    human_number = input("Enter your number : ")
    aiPlayer.targetNumber = (int(human_number[0]),int(human_number[1]),int(human_number[2]),int(human_number[3]))
    
    while not aiPlayer.gameOver:
        move += 1
        prediction = aiPlayer.predict()
        print("PREDICTION",move," : ",prediction[0],prediction[1],prediction[2],prediction[3])
        hint = aiPlayer.giveHint(prediction,aiPlayer.targetNumber)
        print("HINT : ", hint[0],"a ",hint[1],"b")
        aiPlayer.evaluate(hint,prediction)
        
       
        
    print("TOTAL MOVES : ", move)
    print("GAME OVER")
    

if __name__ == '__main__':
    main()
