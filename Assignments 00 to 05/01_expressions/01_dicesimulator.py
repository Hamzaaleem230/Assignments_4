#        **01_expressions**

# 01_dicesimulator
import random

def roll_dice():
    dice1: int = random.randint(1, 6)
    dice2: int = random.randint(1, 6)
    total: int = dice1 + dice2
    print(f"You rolled {dice1} and {dice2}. Total: {total}")
    
def main():
    dice1:int = 10
    print("Starting value of dice1 in main(): " + str(dice1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("Final value of dice1 in main(): " + str(dice1))

    
if __name__ == "__main__":
    main()