#        **01_expressions**

# 05_remainder_division
def reminder():
    num1: int = int(input("Please enter an integer to be divided: "))
    num2: int = int(input("Please enter an integer to divide by: "))
    quotient: int = num1 // num2 
    remainder: int = num1 % num2 
    print(f"The result of the following division is  {quotient}  with the remainder of {remainder}")


if __name__ == '__main__':
    reminder()