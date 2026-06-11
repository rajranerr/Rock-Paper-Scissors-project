import random

def play_game():
    # Define available choices
    choices = ["rock", "paper", "scissors"]
    
    # Initialize game scores
    player_score = 0
    computer_score = 0
    
    print("=== Welcome to Rock, Paper, Scissors! ===")
    print("Rules: Rock beats Scissors | Scissors beats Paper | Paper beats Rock\n")
    
    while True:
        # Get and sanitize player input
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").strip().lower()
        
        if user_choice == 'quit':
            break
            
        if user_choice not in choices:
            print("Invalid choice! Please try again.\n")
            continue
            
        # Generate random computer choice
        computer_choice = random.choice(choices)
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
            
        # Display current standings
        print(f"Score -> You: {player_score} | Computer: {computer_score}\n")
        
    print("\n=== Game Over ===")
    print(f"Final Score -> You: {player_score} | Computer: {computer_score}")
    print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    play_game()