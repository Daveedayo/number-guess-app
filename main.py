import random

get_started = input("Type a number to get started: ")

if get_started.isdigit():
    get_started = int(get_started)

    if get_started <= 0:
        print("Please type a number greater than 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()

start = input("Are you ready to guess the correct number?: ").lower()

if start != "yes":
    quit()

print("Okay! Let's give it a try!") 
random_number = random.randint(0, get_started)

guesses = 0
score = 0

while True:
   guesses += 1
   score += 1

   guess = input('Make a guess: ')
   if guess.isdigit():
        guess = int(guess)
   else:
       print("Please type a number next time")
       continue

   if guess == random_number:
        print("Yes! You got it")
        break
   elif guess < random_number:
       print("Oh! You were below the number")
   else:
        print("Nah! You were above the number")  

if guesses == 1:
    print("You got it in", guesses, "guess")  
else:
    print("You got it in", guesses, "guesses")

if score == 1:
    print("You got", score, "scores")
else:
    print("You got", score, "scores")