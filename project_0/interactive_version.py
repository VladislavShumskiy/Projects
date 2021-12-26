import numpy as np

def play_a_game():
    correct_answer = np.random.randint(1,1001) #creating a random correct answer for the game between 1 and 1000
    counter = 0 # Keeps track of the number of guesses the player takes

    while True:
        player_answer = input('Make a guess:') # Player makes a guess
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("The input must be an integer")
        else:
            counter+=1
            if player_answer == correct_answer:
                print(f"Whoa, nice guess, it took you {counter} tries.")
                break
            elif player_answer > correct_answer:
                print("You guessed too high.")
            else:
                print("You guessed too low.")

if __name__ == "__main__":
    play_a_game()
    
        
print("Game over!")