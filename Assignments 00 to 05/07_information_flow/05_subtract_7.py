#          **07_information_flow**

# 05_subtract_7
def subtract():
	num: int = 7
	num = subtract_seven(num)
	print("this should be zero: ", num)

def subtract_seven(num):
	num = num - 7
	return num


# There is no need to edit code beyond this point

if __name__ == '__main__':
    subtract()