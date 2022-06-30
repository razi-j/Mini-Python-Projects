import random

class rps:
    def __init__(self):
        self.playerScore = 0
        self.AIScore = 0
        self.AIstate = ""

    def AIPick(self):
        states=["rock", "paper", "scissors"]
        self.AIstate = random.choice(states)
        print(self.AIstate)

    def winloss(self,playerChoice):
        if playerChoice != self.AIstate:
            if playerChoice == "rock" and self.AIstate == "scissors":
                print("Player Wins!")
                self.playerScore +=1
                print("Player Score: {}\t\tAI Score: {}".format(self.playerScore, self.AIScore))

        else:
            print("Draw!!")
            self.playerScore += 1
            self.AIScore += 1
