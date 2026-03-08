"""
Docstring for RockPaper
1- Input from user(Rock, paper, scissor)
2- computer choice (computer will choose randomly not conditionally)
3- Result print

cases:
A- Rock
Rock - Rock = tie
Rock - paper = paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor 
Scissor - Scissor = tie
Scissor - rock = rock win
Scissor - paper = Scissor win

"""

import random
item_list = ["Rock","Paper","Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")
 
if user_choice == comp_choice:
    print("Both chooses same: = Match tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer win")
    else:
        print("Rock smashes Scissor = you won")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper, Computer win")   
    else:
        print("paper cover rock, you win")    

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cut paper, You win")
    else:
        print("Rock smashes scissor, Computer win")