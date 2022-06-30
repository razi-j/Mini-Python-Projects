import random
import os

class rps:
    def __init__(self):
        self.playerScore = 0
        self.AIScore = 0
        self.AIstate = ""
        self.playerHand = ""

    def main(self):
        print("-"*60)
        print("\t\t  Rock, Paper, Scissors!!!")
        print("-"*60)
        ch = input("1. Play\n2. Quit\n")
        if ch == "1":
            self.playerChoice()
        elif ch == "2":
            quit()
        else:
            print("Invalid Input")
            self.main()

    def playerChoice(self):
        ch = input("What will you throw? R (rock), P (paper), S (Scissors)?\nnote: Letter only\n")
        hands = ["r", "p", "s"]
        if ch.lower() in hands:
            if ch.lower() == "r":
                self.playerHand = "rock"
            if ch.lower() == "p":
                self.playerHand = "paper"
            else:
                self.playerHand = "scissors"
        else:
            print("Invalid Input!")
            self.playerChoice()

        self.AIPick()
        self.winloss(self.playerHand)


    def AIPick(self):
        states=["rock", "paper", "scissors"]
        self.AIstate = random.choice(states)

    def winloss(self,playerChoice):
        if playerChoice != self.AIstate:
            if playerChoice == "rock" and self.AIstate == "scissors":
                print("Player Wins!")
                print("Player's Hand: {}\t AI's Hand: {}".format(self.playerHand, self.AIstate))
                self.playerScore += 1
            elif playerChoice == "rock" and self.AIstate == "paper":
                print("AI Wins!!")
                print("Player's Hand: {}\t AI's Hand: {}".format(self.playerHand, self.AIstate))
                self.AIScore += 1
            
            if playerChoice == "paper" and self.AIstate == "rock":
                print("Player Wins!")
                print("Player's Hand: {}\t AI's Hand: {}".format(self.playerHand, self.AIstate))
                self.playerScore += 1
            elif playerChoice == "paper" and self.AIstate == "scissors":
                print("AI Wins!!")
                print("Player's Hand: {}\t AI's Hand: {}".format(self.playerHand, self.AIstate))
                self.AIScore += 1

            if playerChoice == "scissors" and self.AIstate == "paper":
                print("Player Wins!")
                print("Player's Hand: {}\t AI's Hand: {}".format(self.playerHand, self.AIstate))
                self.playerScore += 1
            elif playerChoice == "scissors" and self.AIstate == "rock":
                print("AI Wins!!")
                print("Player's Hand: {}\t AI's Hand: {}".format(self.playerHand, self.AIstate))
                self.AIScore += 1

        else:
            print("Draw!!")
            print("Player's Hand: {}\t AI's Hand: {}".format(self.playerHand, self.AIstate))
            self.playerScore += 1
            self.AIScore += 1

        print("Player Score: {}\t\tAI Score: {}".format(self.playerScore, self.AIScore))
        self.restart()

    def restart(self):
        restart = input("Continue Playing? 1. Yes\t 2. No\n")
        if restart == "1":
            os.system("cls")
            self.playerChoice()
        elif restart == "2":
            quit()
        else:
            print("Invalid Input!")

