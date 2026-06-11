import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move: Rock, Paper, Scissor= ")
comp_coice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_coice}")

if user_choice == comp_coice:
    print("Match is tie")
elif user_choice == "Rock":
    if comp_coice == "Paper":
        print("Computer is win")
    else:
        print("You win")

elif user_choice == "Paper":
    if comp_coice == "Scissor":
        print("Computer win")
    else:
        print("You win")
elif user_choice == "Scissor":
    if comp_coice == "Paper":
        print("You win")
    else:
        print("Computer win")