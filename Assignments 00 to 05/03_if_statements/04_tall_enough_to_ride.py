#               **03_if_statements**

# 04_tall_enough_to_ride
MINIMUM_HEIGHT : int = 50 # arbitrary units :)

def ride():
    height = float(input("How tall are you? "))
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You'll be able to ride when you're a little older.")


if __name__ == '__main__':
    ride()