import numpy as np
from statistics import mean

correct_answer = np.random.randint(1,101) # Random number between 1 and 100 which will be the correct answer.

def guess (ans:int)->int:
     """Computer takes random guesses until it lands on the correct answer. Then it outputs  the number of guesses it took to reach it.

     Args:
         ans (int): The correct answer.

     Returns:
         int: number of tries
     """
     counter=0 # counts the number of guesses
     
     while True:
          new_guess = np.random.randint(1,101) # guessing a random number
          counter+=1
          if new_guess==ans:
               break # breaking the cycle if the guess was correct
     
     return counter 

def alg_score(guessing_function, sample_size:int = 100)->int:
     """This function takes in a guessing function and determines what is the average number of tries it takes to reach a correct answer.

     Args:
         guessing_function : Number guessing function.
         sample_size (int, optional): The number of guessing games played to determine the average score. Defaults to 100.

     Returns:
         int: The average score of a guessing function (how many guesses it takes on average to reach the correct answer).
     """
     score_list = []
     
     for i in range (sample_size):
          ans = np.random.randint(1,101) # creating a new correct answer each game
          score_list.append(guessing_function(ans)) #add a score to the list
          
     return mean(score_list) #returns the average of the scores in the list
 
if __name__ == "__main__":
    avg_score = alg_score(guess, 10000)
    print(f'Your algorithm takes an average of {avg_score} tries to reach the correct answer.')