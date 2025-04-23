#          **07_information_flow**

# 01_greetings
def greeting():
    name : str = input("What's your name? ")
    print(greet(name))
    print("Have a nice day!")

def greet(name):
    return "Greetings " + name + "!"
	
if __name__ == '__main__':
    greeting()
