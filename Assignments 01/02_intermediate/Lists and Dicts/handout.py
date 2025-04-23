#           **Lists and Dicts**

# handout

# List Practice
def main():
    # Create a list called fruit_list with the given fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list
    print(f"Length of the list: {len(fruit_list)}")
    
    # Add 'mango' at the end of the list
    fruit_list.append('mango')
    
    # Print the updated list
    print("Updated fruit list:", fruit_list)

if __name__ == "__main__":
    main()


# Index Game
def access_element(lst, index):
    if index < 0 or index >= len(lst):
        return "Index out of range."
    return lst[index]

# Function to modify an element in the list at a given index
def modify_element(lst, index, new_value):
    if index < 0 or index >= len(lst):
        return "Index out of range."
    lst[index] = new_value
    return lst

# Function to slice a list based on start and end indices
def slice_list(lst, start, end):
    if start < 0 or end > len(lst) or start >= end:
        return "Invalid indices."
    return lst[start:end]

# Simple game interaction
def game():
    # Sample list
    my_list = [10, 'apple', 3.14, 'banana', 42]
    
    print("Welcome to the List Index Game!")
    print(f"Initial List: {my_list}")
    
    while True:
        print("\nChoose an operation:")
        print("1: Access an element")
        print("2: Modify an element")
        print("3: Slice the list")
        print("4: Exit the game")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            # Accessing an element
            index = int(input("Enter the index of the element to access: "))
            result = access_element(my_list, index)
            print(f"Element at index {index}: {result}")
        
        elif choice == '2':
            # Modifying an element
            index = int(input("Enter the index of the element to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(my_list, index, new_value)
            print(f"Updated list: {result}")
        
        elif choice == '3':
            # Slicing the list
            start = int(input("Enter the start index for slicing: "))
            end = int(input("Enter the end index for slicing: "))
            result = slice_list(my_list, start, end)
            print(f"Sliced list: {result}")
        
        elif choice == '4':
            print("Exiting the game. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    game()
