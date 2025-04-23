#        **01_expressions**

# 02_e=mc2
def energy():
    c: float = 299792458
    m: float = float(input("Enter Kilos of mass: "))
    print("e = m*c^2")
    print("Mass = " + str(m) + " kg")
    print("C = " + str(c) + " m/s")
    print("e = " + str(m * c **2) + " jules")
    
if __name__ == '__main__':
    energy()