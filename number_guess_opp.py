import random

def game():
  # generate a random number between 1 and 10
  secret_num = int(input("Pick a secret number between 1 and 10: "))
  guesses = []
  
  start, end = 1, 10
  while len(guesses) < 5:
    # get a number guess from the computer
    guess = random.randint(start,end)
    print("Computer guessed: {}".format(guess))
    # compare guess to secret number
    if guess == secret_num:
      print("You got it: My number was {}".format(secret_num))
      break
    elif guess < secret_num:
      print("My number is higher than {}".format(guess))
      if len(guesses) == 0: 
        start, end = guess + 1, 10
        prev_high = 10
      else:
        start, end = guess + 1, prev_high - 1
      prev_low = guess
    elif guess > secret_num:
      print("My number is lower than {}".format(guess))
      if len(guesses) == 0: 
        start, end = 1, guess - 1
        prev_low = 1
      else:
        start, end = prev_low + 1, guess - 1
      prev_high = guess
    else:
      print("That's not it")
    guesses.append(guess)
  else:
    print("You didn't get it! My number was {}".format(secret_num))
  play_again = input("Do you want to play again? Y/n ")
  if play_again.lower() != 'n':
    game()
  else:
    print("Bye!")

game()