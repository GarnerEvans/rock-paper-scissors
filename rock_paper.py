#have user and computer
#ask user for input
#if valid input from list of rock paper scissor choices - continue
#if invalid repeat question
#prompt comp class to choose option then compare the two sselctions
#display corresponding message for each pairing
from random import randint

choices = ['rock', 'paper', 'scissors']

class player:
    def __init__(self):
        self.decision = "None"
        self.score = 0

    def playerMove(self, choice, run):
        x = 0
        for i in range(3):
            if choice == choices[i]:
                x = 1
        if x == 0:
            print("Thanks for playing!")
            run = False
    
            
        if x == 1:
            self.decision = choice
            return run

    def check(self, comp_choice):
        if self.decision != "None":
            if self.decision == "rock" and comp_choice == "paper":
                print("The computer has won, better luck next time!")
            elif self.decision == "paper" and comp_choice == "rock":
                print("You have won, good job!")
            if self.decision == "rock" and comp_choice == "scissors":
                print("You have won, good job!")
            elif self.decision == "scissors" and comp_choice == "rock":
                print("The computer has won, better luck next time!")
            if self.decision == "paper" and comp_choice == "scissors":
                print("The computer has won, better luck next time!")
            elif self.decision == "scissors" and comp_choice == "paper":
                print("You have won, good job!")

    # def returnScore(self):
    #     return self.score

player_1 = player()
#running methods
run = True
while run == True:
    player_1.playerMove(input("Please enter a choice:"), run)
    if run == True:
        comp_choice = choices[randint(0, 2)]
        print(f"The computer has chosen {comp_choice}")
        player_1.check(comp_choice)
    # print(player_1.returnScore())

