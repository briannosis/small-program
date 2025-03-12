import random

"""
Documentation:

The program will prompt the user to pick a number between 1 and 3:
1 represents the Rock, 2 represents the Paper, and 3 represents the Scissors.
The computer will generate a random number,
and it will be used as an index to access the element inside the array.
The player's input will be compared to the element,
and the outcome will be decided based on the game logic:

*Rock (1) > Scissors (3)
*Scissors (3) > Paper (2)
*Paper (2) > Rock (1)

Each array has been set in accordance with the player's input
so that whenever a player selects a number,
fitting choices will be made.
"""

#Sets the probability of computer; losing is 5 out of 10, 2 out of 10 for draw, and 3 out of 10 in winning
easy_diff_rock = [3, 1, 2, 3, 2, 1, 3, 3, 2, 3]
easy_diff_paper = [1, 2, 1, 3, 1, 2, 3, 1, 1, 3]
easy_diff_scissors = [2, 3, 2, 1, 2, 1, 2, 1, 2, 3]

#Sets the probability of computer; losing 1 in 10, 5 out of 10 for draw, and 4 out of 10 in winning
hard_diff_rock = [3, 1, 2, 1, 2, 1, 2, 2, 1, 1]
hard_diff_paper = [1, 2, 3, 2, 3, 2, 2, 2, 3, 3]
hard_diff_scissors = [2, 3, 1, 1, 3, 1, 3, 1, 3, 3]

computer_pick = None
player_score = 0
computer_score = 0

def easy_difficulty(computer_pick, player_input, player_score, computer_score):
    #Rock
    if player_input == 1:
        computer_pick = easy_diff_rock[random_number]
        if player_input == 1 and computer_pick == 2:
            computer_score +=1
            print("Computer Wins!\nPlayer Picks: ", player_input, "Computer Picks: ", computer_pick)
            print("Player Score: ", player_score, "Computer Score: ", computer_score)
        elif player_input == 1 and computer_pick == 3:
            player_score +=1
            print("Player Wins!\nPlayer Picks: ", player_input, "Computer Picks: ", computer_pick)
            print("Player Score: ", player_score, "Computer Score: ", computer_score)
        else:
            print("Draw")
            print("Player Score: ", player_score, "Computer Score: ", computer_score)
    #Paper
    elif player_input == 2:
        computer_pick = easy_diff_paper[random_number]
        if player_input == 2 and computer_pick == 3:
            computer_score +=1
            print("Computer Wins!\nPlayer Picks: ", player_input, "Computer Picks: ", computer_pick)
            print("Player Score: ", player_score, "Computer Score: ", computer_score)
        elif player_input == 2 and computer_pick == 1:
            player_score +=1
            print("Player Wins!\nPlayer Picks: ", player_input, "Computer Picks: ", computer_pick)
            print("Player Score: ", player_score, "Computer Score: ", computer_score)
        else:
            print("Draw")
            print("Player Score: ", player_score, "Computer Score: ", computer_score)
    
    elif player_input == 3:
        computer_pick = easy_diff_scissors[random_number]
        if player_input == 3 and computer_pick == 1:
            computer_score +=1
            print("Computer Wins!\nPlayer Picks: ", player_input, "Computer Picks: ", computer_pick)
            print("Player Score: ", player_score, "Computer Score: ", computer_score)
        elif player_input == 3 and computer_pick == 2:
            player_score +=1
            print("Player Wins!\nPlayer Picks: ", player_input, "Computer Picks: ", computer_pick)
            print("Player Score: ", player_score, "Computer Score: ", computer_score)
        
        else:
            print("Draw!\n Player Picks: ", player_input, "Computer Picks: ", computer_pick)
            print("Player Score: ", player_score, "Computer Score: ", computer_score)
    else:
        print("Invalid Pick")

def hard_difficulty(difficulty):
    pass


print("\n\nROCK PAPER SCISSORS!")
difficulty_option = input("Select the difficulty: Type 'E' for Easy\n Type 'H' for Hard\n Input: ")

while player_score != 3 or computer_score != 3:
    print("\n\nROCK PAPER SCISSORS!")
    player_input = int(input("SELECT\n 1. ROCk\n 2. PAPER\n 3. SCISSORS \n Yourpick: "))
    random_number = random.randint(0,9)

    easy_difficulty(computer_pick, player_input, player_score, computer_score)

    if player_score == 3 or computer_score == 3:
        break





"""
if player_input == 1:
        computer_pick = easy_diff_rock[random_number]
        if player_input == 1 and computer_pick == 2:
            computer_score +=1
            print("Computer Wins!\nPlayer Picks: ", player_input, "Computer Picks: ", computer_pick)
            print("Player Score: ", player_score, "Computer Score: ", computer_score)
        elif player_input == 1 and computer_pick == 3:
            player_score +=1
            print("Player Wins!\nPlayer Picks: ", player_input, "Computer Picks: ", computer_pick)
            print("Player Score: ", player_score, "Computer Score: ", computer_score)
        else:
            print("Draw")
            print("Player Score: ", player_score, "Computer Score: ", computer_score)
    #Paper
    elif player_input == 2:
        computer_pick = easy_diff_paper[random_number]
        if player_input == 2 and computer_pick == 3:
            computer_score +=1
            print("Computer Wins!\nPlayer Picks: ", player_input, "Computer Picks: ", computer_pick)
            print("Player Score: ", player_score, "Computer Score: ", computer_score)
        elif player_input == 2 and computer_pick == 1:
            player_score +=1
            print("Player Wins!\nPlayer Picks: ", player_input, "Computer Picks: ", computer_pick)
            print("Player Score: ", player_score, "Computer Score: ", computer_score)
        else:
            print("Draw")
            print("Player Score: ", player_score, "Computer Score: ", computer_score)
    
    elif player_input == 3:
        computer_pick = easy_diff_scissors[random_number]
        if player_input == 3 and computer_pick == 1:
            computer_score +=1
            print("Computer Wins!\nPlayer Picks: ", player_input, "Computer Picks: ", computer_pick)
            print("Player Score: ", player_score, "Computer Score: ", computer_score)
        elif player_input == 3 and computer_pick == 2:
            player_score +=1
            print("Player Wins!\nPlayer Picks: ", player_input, "Computer Picks: ", computer_pick)
            print("Player Score: ", player_score, "Computer Score: ", computer_score)
        
        else:
            print("Draw!\n Player Picks: ", player_input, "Computer Picks: ", computer_pick)
            print("Player Score: ", player_score, "Computer Score: ", computer_score)
    else:
        print("Invalid Pick")
"""