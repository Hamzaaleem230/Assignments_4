#           **06_functions**

# 00_averages
def average(a: float, b: float):
    """
    Returns the average of a and b
    """
    sum = a + b
    return sum / 2

def averages():
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    final = average(avg_1, avg_2)
    print("avg_1", avg_1)
    print("avg_2", avg_2)
    print("final", final)


if __name__ == '__main__':
    averages()