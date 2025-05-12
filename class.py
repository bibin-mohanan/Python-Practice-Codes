# Create a class named flashcard. Initialize dictionary fruits using the init() method

import random
class Flashcard:
    def __init__(self):
        self.dict= {'apple':'red',
                    'orange':'orange',
                    'watermelon':'green',
                    'banana':'yellow'}
    def choice(self) :
        while (True):
            fruit,color = random.choice(list(self.dict.items()))
            guess = input( "What is the color of {} :". format(fruit))
            if (guess.lower()==color):
                print("Correct answer")
            else:
                print("Wrong answer")
            option = int(input( "enter 0, to play again :"))
            if (option):
                break
print("Guess the color")
fc=Flashcard()
fc.choice()