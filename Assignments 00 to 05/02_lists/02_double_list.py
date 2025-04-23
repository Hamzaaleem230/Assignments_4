#          ** 02_lists **

# 02_double_list
def double_list():
    numbers: list[int] = [1, 2, 3, 4]  # Create a list of integers
    for i in range(len(numbers)):  # Loop through the length of the numbers list
        elem_at_index = numbers[i]  # Get the element at index i
        numbers[i] = elem_at_index * 2  # Double the element

    print(numbers)  # Print the list


if __name__ == '__main__':
    double_list()