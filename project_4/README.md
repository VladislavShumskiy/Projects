# Project 0. Guess the number


## Contents
[1. Project description](#project-description)  
[2. Case being solved](#case-being-solved)  
[3. Brief data information](#brief-data-information)  
[4. Steps in the work on the project](#steps-in-the-work-on-the-project)  
[5. Result](#result)  
[6. Conclusions](#conclusions)


### Project description
The task is to guess the random number from 1 to 100 as fast as possible.

:arrow_up: [To the contents](#contents)


### Case being solved
It's required to write a program capable of guessing a random number in the minimal number of tries.

**Conditions:**  
- Computer creates a random number from 1 to 100 and we need to guess it.
- When an algorythm makes a guess it recieves information about answer being higher or lower than it.

**Result metrics:**  
The result is judjed by the number of tries it takes our program to reach the correct result on average given 1000 attempts.

**Three algorythms are being compared:**
- The first one takes random guesses untill it stumbles upon a correct answer.  
- The second one rakes random guesses while taking into account whether the last guess was higher or lower than the correct answer.  
- The third one does a binary search for a correct answer.

:arrow_up: [To the contents](#contents)


### Brief data information
....

:arrow_up: [To the contents](#contents)


### Steps in the work on the project
....

:arrow_up: [To the contents](#contents)


### Result
**Algorythms average scores:**
- Random guessing ~ 100
- Improved random guessing ~ 7.5
- Binary search ~ 5.8

:arrow_up: [To the contents](#contents)


### Conclusions
Random guessing takes on average as many tries as there are total possibilities for the correct answer, as expected.
While taking into account the relative position of the answer relative to the guess at each random guess drastically reduces the number of steps required it is still more efficient to use the binary search.

:arrow_up: [To the contents](#contents)