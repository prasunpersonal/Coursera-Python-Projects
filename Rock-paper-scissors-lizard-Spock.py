import math
import random

def nameToNumber(name):
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    else:
        number = 4
    return number

def numberToName(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    else:
        name = "scissors"
    return name
    

def game(player_choice):
    print("")
    
    print("Player chooses " + player_choice)
    
    playerNumber = nameToNumber(player_choice)
    
    computerNumber = random.randrange(0, 5)
    
    computerChoice = numberToName(computerNumber)
    
    print("Computer chooses " + computerChoice)
    
    difference = ((playerNumber - computerNumber) % 5)
    
    if difference == 1 or difference == 2:
        print("Player wins!")
    elif difference == 3 or difference == 4:
        print("Computer wins!")
    else:
        print("Player and computer tie!")
    return ""
    
game("rock")
game("Spock")
game("paper")
game("lizard")
game("scissors")