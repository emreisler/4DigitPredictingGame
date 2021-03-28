# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from AiPlayer import Ai

def main():

    toplamHamleSayisi = 0
    #totalGAmes = 50
    #for i in range(totalGAmes):
    hamle = 0
    aiPlayer = Ai()
    human_number = input("Enter your number : ")
    aiPlayer.targetNumber = (int(human_number[0]),int(human_number[1]),int(human_number[2]),int(human_number[3]))
    while not aiPlayer.gameOver:
        hamle += 1
        prediction = aiPlayer.predict()
        print("PREDICTION : ",prediction[0],prediction[1],prediction[2],prediction[3])
        hint = aiPlayer.giveHint(prediction,aiPlayer.targetNumber)
        print("HINT : ", hint[0],"a ",hint[1],"b")
        aiPlayer.evaluate(hint,prediction)
        #print(aiPlayer.tumOlasiliklar)
        aiPlayer.normalize()
        #aiPlayer.evaluate(prediction)
        aiPlayer.zeroPossibilitesList()
    print("TOTAL MOVES : ", hamle)
    print("GAME OVER")
    toplamHamleSayisi += hamle
    #print("ORTALAMA KAÇ HAMLEDE BULDU : ", toplamHamleSayisi / totalGAmes )

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
