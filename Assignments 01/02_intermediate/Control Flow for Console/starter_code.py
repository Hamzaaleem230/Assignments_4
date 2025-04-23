#        **Control Flow for Console**

# starter_code
import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    score = 0  # Start score from 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        your_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is {your_number}")
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

        # Input validation
        while guess != "higher" and guess != "lower":
            guess = input("Please enter either higher or lower: ").lower()

        # Game logic
        if your_number > computer_number and guess == "higher":
            print("You were right!", end=' ')
            score += 1
        elif your_number < computer_number and guess == "lower":
            print("You were right!", end=' ')
            score += 1
        else:
            print("Aww, that's incorrect.", end=' ')

        print(f"The computer's number was {computer_number}")
        print(f"Your score is now {score}")
        print()  # Empty line between rounds

    # End message
    print("Thanks for playing!")

    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Run the main function
if __name__ == "__main__":
    main()
