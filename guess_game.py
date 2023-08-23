import random 

guessnumbers = random.randint(1,6)
print("I am thinking of a Number between 1 and 5. Guess the number!")



while True:
	user_guess = int(input("Number is: "))
	if user_guess > 6:
		print("Wrong! That's more than 6 ")
	elif user_guess < 0:
		print("Nop! that's out of range!")
	elif user_guess != guessnumbers:
		print("Almost there! but wrong! ")
	elif user_guess == guessnumbers:
		print("woohoo! Correct")

		break

