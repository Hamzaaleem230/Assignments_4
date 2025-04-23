#           **04_dictionaries**

# 00_count_nums
def get_user_numbers():
    """
    Create an empty list.
    Loop over the user input. 
    If the user enters a blank line, break out of the loop and stop asking for input.
    If the user enters a number, convert it to an integer and add it to the list.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        
        # if the user enters a blank line, break out of the loop
        if user_input == "":
            break
        
        # if the user enters a number, convert it to an integer and add it to the list
        num = int(user_input)
        user_numbers.append(num)
    
    return user_numbers

def count_nums(num_lst):
    """
    Create an empty dictionary.
    Loop over the list of numbers and add each number as a key to the dictionary. If the number is already in the dictionary, increment its value by 1.
    """
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    return num_dict


def print_counts(num_dict):
    """
    Loop over the dictionary and print out the number of times each number appears.
    """
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")


def main():
    """
    Call the get_user_numbers and count_nums functions
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)


# Call the main function
if __name__ == '__main__':
    main()