# 01_expressions

# 07_tiny_mad_lib
sentence_start: str = "I learned to program and used Python to create a"

def mad_lib():
    noun: str = input("Please type a noun: ")
    adjective: str = input("Please type an adjective: ")
    verb: str = input("Please type a verb: ")
    
    # Ensure there's proper spacing and sentence flow
    print(f"{sentence_start} {adjective} {noun} that {verb}!")

if __name__ == '__main__':
    mad_lib()
