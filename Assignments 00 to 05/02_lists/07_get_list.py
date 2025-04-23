#          ** 02_lists **

# 07_get_list
def get_list():
    list = []  # Create an empty list

    val = input("Enter a value: ")  # Get the first value
    while val:  # Loop while val is not empty
        list.append(val) # Add val to list
        val = input("Enter a value: ")  # Get the next value

    print("Here's the list:", list)



if __name__ == '__main__':
    get_list()