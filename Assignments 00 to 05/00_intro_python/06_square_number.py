#       ** 00_intro_python **

# 06_square_number
def square():
    print("This program squares a number.")
    num1:int = int(input("Enter a number and I will square it. "))
    print(f"The square of {num1} is {num1 ** 2}")
    

if __name__ == '__main__':
    square()