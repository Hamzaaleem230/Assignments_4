#             **05_loops_control_flow**

# 03_wholesome_machine
AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def wholesome_machine():
    print("Please type the following affirmation: " + AFFIRMATION)

    user_feedback = input()  # Get the user's input
    while user_feedback != AFFIRMATION:  # While the user did not type the affirmation correctly
        # Tell the user that they were wrong
        print("That was not the affirmation.")

        # Ask the user to type the affirmation
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()

    print("That's right! :)")


if __name__ == '__main__':
    wholesome_machine()