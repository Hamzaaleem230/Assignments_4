#           **06_functions**

# 07_print_multiple
def print_multiple(message: str, repeats: int):
    for i in range(repeats):
        print(message, end=' ')

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()
