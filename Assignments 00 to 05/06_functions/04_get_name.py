#           **06_functions**

# 04_get_name
def get_name():
    return "Sophia"


def get_name():
    name = get_name() # get_name() will return a string which we store to the 'name' variable here
    print("Howdy", name, "! 🤠")

if __name__ == '__main__':
    get_name()