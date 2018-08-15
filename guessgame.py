#Pratik

guess_word="Pratik"
guess=""
guess_count=0
guess_limit=5
out_of_guesses=False

while guess != guess_word and not(out_of_guesses):
      if guess_count < guess_limit:
          guess=input("Enter guess: ")
          guess_count+=1
      else:
          out_of_guesses=True
          if out_of_guesses:
              print("You loose the game")
else:
              print("You win")
