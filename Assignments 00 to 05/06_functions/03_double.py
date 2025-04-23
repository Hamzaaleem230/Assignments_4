#           **06_functions**

# 03_double
def double(num: int):
    return num * 2


def double():
    num = int(input("Enter a number: "))
    num_times_2 = double(num)
    print("Double that is", num_times_2)

if __name__ == '__main__':
    double()