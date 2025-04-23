#       ** 00_intro_python **

# 01_add_two_numbers
def add():
    print("This program adds two numbers.")
    first_number : int = int(input("Enter first number: "))
    second_number : int = int(input("Enter second number: "))
    total: int = int((first_number + second_number))
    print(f"The total sum of {first_number} + {second_number} = {total}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    add ()