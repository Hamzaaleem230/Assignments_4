#           **01_basics**

# 01_double_it
def main():
    curr_value = int(input("Enter a number: "))
    curr_value = curr_value * 2  # first doubling

    while curr_value < 100:
        print(curr_value, end=' ')
        curr_value = curr_value * 2

    print(curr_value)  # Print the final value that is >= 100


if __name__ == '__main__':
    main()
