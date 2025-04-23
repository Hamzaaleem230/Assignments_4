#             **05_loops_control_flow**

# 00_guess_my_number
import random

def guess_my_number():
    # Generate a random number
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")
    
    # Get a guess from the user
    guess = int(input("Enter a guess: "))
    # Loop until the guess is correct
    while guess != secret_number:
        if guess < secret_number:  # Check if the guess is too low
            print("Your guess is too low")
        else:
            print("Your guess is too high")
            
        print() # Print an empty line
        guess = int(input("Enter a new guess: "))  # Get a new guess
        
    print("Congrats! The number was: " + str(secret_number))
    
if __name__ == '__main__':
    guess_my_number()