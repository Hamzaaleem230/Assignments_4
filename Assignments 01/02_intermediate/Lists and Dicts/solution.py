#           **Lists and Dicts**

# solution
# Index Game Solution
def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices."

def index_game():
    lst = [1, 2, 3, 4, 5]  # Example list
    print("Current list:", lst)
    
    while True:
        print("\nChoose an operation: access, modify, slice, or quit")
        operation = input("Enter operation: ").strip().lower()
        
        if operation == "access":
            try:
                index = int(input("Enter index to access: "))
                print(access_element(lst, index))
            except ValueError:
                print("Invalid input. Please enter a valid integer index.")
                
        elif operation == "modify":
            try:
                index = int(input("Enter index to modify: "))
                new_value = input("Enter new value: ")
                print(modify_element(lst, index, new_value))
            except ValueError:
                print("Invalid input. Please enter a valid integer index.")
                
        elif operation == "slice":
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                print(slice_list(lst, start, end))
            except ValueError:
                print("Invalid input. Please enter valid integer indices.")
                
        elif operation == "quit":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid operation. Please choose one of: access, modify, slice, or quit.")

index_game()



# List Practice Solution
def main():
    # Create a list called fruit_lst with the given fruits
    fruit_lst = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list
    lst_length = len(fruit_lst)
    print(f"Length of the list: {lst_length}")
    
    # Add 'mango' at the end of the list
    fruit_lst.append('mango')
    
    # Print the updated list
    print("Updated fruit list:")
    for fruit in fruit_lst:
        print(fruit)

if __name__ == "__main__":
    main()
