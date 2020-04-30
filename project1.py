# Generate Random Number
import random
# Introduce Game
def start_game():
    print("This is a game where you pick a number 1 through 10")
# Play the game
def play_game():
    random_number = random.randint(1,10)
    attempts = 0
    while True:
        try:
            guess_number = int(input("\nEnter a number between 1 and 10: "))
        except:
            print("Sorry wrong input. Remember only numbers between 1 and 10.")
        else:
            if guess_number == random_number:
                attempts += 1
                print(f"Congradulations {random_number} was the right number! It took you {attempts} to get it right.")
                break
            elif guess_number < random_number and guess_number >= 1:
                attempts += 1
                print(f"Sorry {guess_number} is lower than the right number. Please try again\n")
                continue
            elif guess_number > random_number and guess_number <= 10:
                attempts += 1
                print(f"Sorry {guess_number} is higher than the right number. Please try again\n")
                continue
            else:
                print(f"Your guess of {guess_number} was outside the range. Remember we are playing from 1 to 10.")
                continue
            print("\nYou have finished the game.")

# Play another Game
def another_game():
    while True:
        play_again = input("\nWould you like to play again? (yes or no?)")
        if play_again.lower() == "yes":
            play_game()
            continue
        elif play_again.lower() == "no":
            print("Thanks for playing. Hoper to see you soon.")
            break
        else:
            print("\nInvalid Input. Please Try Again.")
            continue

# Game all put together
start_game()
while True:
    want_to_play = input("\nWould you like to play the game? yes or no? ")
    if want_to_play.lower() == "yes":
        play_game()
        another_game()
        break
        print("Thanks for playing the game. Hope to see you soon!")
    elif want_to_play.lower() == "no":
        print("Hope to see you again.")
        break
    else:
        print("Sorry Invalid Input.")
        continue
