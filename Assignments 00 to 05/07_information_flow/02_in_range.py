#          **07_information_flow**

# 02_in_range
def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True

    # we could have also included an else statement, but since we are returning, it's fine without!
    return False

    # return n >= low and n <= high