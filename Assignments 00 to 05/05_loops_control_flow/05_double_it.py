#             **05_loops_control_flow**

# 05_double_it
def double_it():
    curr_value = int(input("Enter a number: "))
    curr_value = curr_value * 2  # first doubling
    while curr_value < 100:
        print(curr_value, end=' ')
        curr_value = curr_value * 2
    print(curr_value)  # print the final value >= 100


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    double_it()
