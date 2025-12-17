import random

def get_user_choice():
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter your choice (1/2/3): ")
    return choice

def get_computer_choice():
    return random.choice(['1', '2', '3'])

def choice_name(choice):
    if choice == '1':
        return "Rock"
    elif choice == '2':
        return "Paper"
    else:
        return "Scissors"

def check_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == '1' and computer == '3') or \
         (user == '2' and computer == '1') or \
         (user == '3' and computer == '2'):
        return "user"
    else:
        return "computer"

user_score = 0
computer_score = 0

while True:
    user_choice = get_user_choice()

    if user_choice not in ['1', '2', '3']:
        print("Invalid choice! Try again.")
        continue

    computer_choice = get_computer_choice()

    print("\nYou chose:", choice_name(user_choice))
    print("Computer chose:", choice_name(computer_choice))

    result = check_winner(user_choice, computer_choice)

    if result == "user":
        print("You win this round!")
        user_score += 1
    elif result == "computer":
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("This round is a draw!")

    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("\nThanks for playing Rock, Paper, Scissors!")
        break
