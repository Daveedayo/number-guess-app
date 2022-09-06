import random

get_started = input("Type a number to get started: ")

if get_started.isdigit():
    get_started = int(get_started)
    print("Cool...")

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
random_number = random.randint(0, 11)
