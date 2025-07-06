import random

def rock_paper_scissors():
    option = ['rock', 'paper', 'scissors']

    while True:
        choice = input('Choose rock, paper, or scissors: ').lower()
        computer_choice = random.choice(option)

        if choice not in option:
            print(' Invalid choice, please try again.')
            continue

        print(f'You chose {choice}, and the computer chose {computer_choice}.')

        if choice == computer_choice:
            print("⚖️ It's a tie!")
        elif (choice == 'rock' and computer_choice == 'scissors') or \
             (choice == 'paper' and computer_choice == 'rock') or \
             (choice == 'scissors' and computer_choice == 'paper'):
            print(" You win!")
        else:
            print(" You lose!")

        play_again = input('Do you want to play again? (y/n): ').strip().lower()
        if play_again != 'y':
            print("👋 Thanks for playing!")
            break

# Run the game
rock_paper_scissors()
