#        **01_expressions**

# 04_pythagorean_theorem
import math

def triangle():
    ab: float = float(input("Enter the length of the side AB: "))
    ac: float = float(input("Enter the length of the side AC: "))
    bc: float = math.sqrt(ab**2 + ac**2)
    print(f"The length of BC (the hypotenuse is : {bc})")


if __name__ == '__main__':
    triangle()