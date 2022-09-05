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

random_number = random.randint(0, 11)
