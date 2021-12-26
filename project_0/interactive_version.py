import numpy as np

correct_answer = np.random.randint(1,101) #creating a random correct answer for the game between 1 and 100
counter = 0 # Keeps track of the number of guesses the player takes

while True:
    player_answer = input('Make a guess:') # Player makes a guess.
    try:
        player_answer = int(player_answer) # Checking if the input is an integer.
    except ValueError:
        print("The input must be an integer")
    else:
        counter+=1
        if player_answer == correct_answer:
            print(f"Whoa, nice guess, it took you {counter} tries.")
            break # Break a cycle if the player guessed correctly.
        elif player_answer > correct_answer:
            print("You guessed too high.")
        else:
            print("You guessed too low.")

print("Game over!")