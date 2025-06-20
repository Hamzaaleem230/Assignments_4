#             **05_loops_control_flow**

# 01_fibonacci
MAX_TERM_VALUE : int = 10000

def fibonacci():
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next


if __name__ == '__main__':
    fibonacci()