from typing import Counter
import numpy as np
from statistics import mean

correct_answer = np.random.randint(1,101) # Random number between 1 and 100 which will be the correct answer.

def random_guess (ans:int)->int:
     """Computer takes random guesses until it lands on the correct answer.
     Then it outputs  the number of guesses it took to reach it.

     Args:
         ans (int): The correct answer.

     Returns:
         int: The number of tries.
     """
     counter=0 # Counts the number of guesses.
     
     while True:
          new_guess = np.random.randint(1,101) # Guessing a random number.
          counter+=1
          if new_guess==ans:
               break # Breaking the cycle if the guess was correct.
     
     return counter 
 
def improved_random_guess(ans:int)->int:
    """Computer takes a random guess from lower to upper bounds (1 and 100 at the start).
    Then knowing whether the correct answer is bigger or smaller than the initial guess
    replaces either the lower or the upper bound with this guess and makes another random guess with updated bounds.
    Repeats until the answer is found.

    Args:
        ans (int): The correct answer.

    Returns:
        int: The number of tries.
    """
     
    counter = 0 # Counts the number of guesses.
    upper_bound = 100
    lower_bound = 1
     
    while True:
        counter+=1
        new_guess = np.random.randint(lower_bound,upper_bound+1) # Taking a random guess in set bounds.
        if new_guess==ans:
            break # Break a cycle if the guess is correct.
        elif new_guess < ans: # If a guess is lower than the answer then the lower bound for the next random number is set to the value of this guess so that the new guess will be higher than it.
            lower_bound = new_guess+1
        else: # If a guess is higher than the answer then the upper bound for the next random number is set to the value of this guess so that the new guess will be lower than it.
            upper_bound = new_guess-1
    
    return counter

def binary_search(ans:int)->int:
    """Does a binary search for a number.

    Args:
        ans (int): The correct answer.

    Returns:
        int: The number of tries.
    """
    
    counter = 0 # Counts the number of guesses.
    upper_bound = 100
    lower_bound = 1
    
    while True:
        guess = int((upper_bound+1+lower_bound)/2)
        counter+=1
        
        if guess==ans:
            break
        elif guess < ans:
            lower_bound = guess+1
        else:
            upper_bound = guess-1
    
    return counter
    
def alg_score(guessing_function, sample_size:int = 1000)->int:
    """This function takes in a guessing function and determines what is the average number of tries it takes to reach a correct answer.

    Args:
        guessing_function : Number guessing function.
        sample_size (int, optional): The number of guessing games played to determine the average score. Defaults to 1000.

    Returns:
        int: The average score of a guessing function (how many guesses it takes on average to reach the correct answer).
    """
    score_list = []
    
    for i in range (sample_size):
         ans = np.random.randint(1,101) # creating a new correct answer each game
         score_list.append(guessing_function(ans)) #add a score to the list
    
    score=mean(score_list)
    print(f'Your algorithm takes an average of {score} tries to reach the correct answer.')     
    return score #returns the average of the scores in the list