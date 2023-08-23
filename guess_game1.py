import random

# Using a for loop
while True:
    secret_number = random.randint(1, 10)
    print("I am thinking of a number between 1 and 10")


    for guess_taken in range(1, 7):
        guess = int(input("Take a guess: "))

        if guess > secret_number:
            print("Your guess is too high")
        elif guess < secret_number:
            print("Your guess is too low")
        else:
            print("Correct! You guessed my number in "+ str(guess_taken) +  " guesses")
            break
    else:
        print("Nope, the number I was thinking was " + str(secret_number))
        
        
    play_again = input("Would you like to play again? ")

    if play_again != "yes":
        print("Bye and Thanks!")
        break
