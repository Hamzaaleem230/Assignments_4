#       ** 00_intro_python **

# 05_triangle_perimeter
def triangle():
    print("This code is about perimeter of triangle.")
    side1: float = float(input("What is the length of side 1 triangle? "))
    side2: float = float(input("What is the length of side 2 triangle? "))
    side3: float = float(input("What is the length of side 3 triangle? "))
    total: float = float(side1 + side2 + side3)
    print(f"The perimeter of the triangle is {total}")
    

if __name__ == '__main__':
    triangle()