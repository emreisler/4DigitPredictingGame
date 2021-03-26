# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from AiPlayer import Ai

def main():


    for i in range(90):
        hamle = 0
        aiPlayer = Ai()
        while not aiPlayer.gameOver:
            hamle += 1
            prediction = aiPlayer.predict()
            print("PREDICTION : ",prediction)
            hint = aiPlayer.giveHint(prediction)
            print(hint)
            aiPlayer.evaluate(hint,prediction)
            print(aiPlayer.tumOlasiliklar)
            aiPlayer.normalize()
            #aiPlayer.evaluate(prediction)
        print("HAMLE SAYISI : ", hamle)
        print("GAME OVER")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
