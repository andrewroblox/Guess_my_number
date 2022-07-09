print("star to kserve/kserve to start")
import random
# selects a random number between 1 and 100
number = random.randint(1,100)
number_of_guesses = 0
while number_of_guesses < 20:
  guess = int(input("please enter your guess dude"))
  if guess == number:
    print("fine you win ")
    break   
  elif guess < number:
    print("To SMALLL🤣🤣🤣!!!!Guess again")
  elif guess > number:
    print("TO BIGGG🤢guess agian")
  number_of_guesses += 1
