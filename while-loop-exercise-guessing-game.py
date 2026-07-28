print('===== GUESSING GAME ====') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
# Three Loop Questions:
#1. What do I want to repeat?
#  -> "Try again, x more guesses"
#2. What do I want to change each time?
#  -> How many guesses they have left
#3. How long should we repeat?
#  -> untill they hit 3 guesses

i = 0
print("Try to guess the number I'm thinking of (1-100)! You get 5 guesses.")

while i < 5:
        num = 50
        print(f"You have {5 - i} gueses remaining!")
        guess = int(input("Your guess: "))
        i+=1
        if guess == num:
            print(f"Congrats, your guess {guess} was correct!")
            print("==== GAME OVER ====")
            break
        elif guess > num:
              print(f"You guessed too high!")
        elif guess < num:
              print(f"You guessed too low!")
else:
      print("You did not guess correctly!")
      print("==== GAME OVER ====")
