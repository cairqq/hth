# Guessing game - Carina Bui 

import random

def generate_random_number(): #generates a random
    return int(random.randint(1,100))

def get_user_guess(): #loop that grabs the users guess (the main game) and compares to target number 
    target_number = generate_random_number()
    while True:
        try:    
            get_user_guessed = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("enter a valid integer")
            continue

        if get_user_guessed == target_number:
            print("congrats! you guessed the number!")
            break
        elif get_user_guessed < target_number:
            print("too low try again!")
            user_exit = input("Enter 'exit' to quit or continue entering guesses: ")
            if user_exit.lower() == 'exit':
                print("Exiting the game. Goodbye!")
                break
        elif get_user_guessed > target_number:
            print("too high try again")
            user_exit = input("Enter 'exit' to quit or continue entering guesses: ")
            if user_exit.lower() == 'exit':
                print("Exiting the game. Goodbye!")
                break
        else:
            print("wrong! try again")
            user_exit = input("Enter 'exit' to quit or continue entering guesses: ")
            if user_exit.lower() == 'exit':
                print("Exiting the game. Goodbye!")
                break

get_user_guess()

def play_guessing_game(): # the start 
    print("welcome to number guessing game")
    get_user_guess()
    print("thanks for playing")

def game_loop(): # calls the game loop
    play_guessing_game()

if __name__ == "__main__": 
    game_loop()
