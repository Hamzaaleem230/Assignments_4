#          **07_information_flow**

# 03_in_stock
def main():
	fruit : str = input("Enter a fruit: ")
	stock = num_in_stock(fruit)
	if stock == 0:
		print("This fruit is not in stock.")
	else:
		print("This fruit is in stock! Here is how many:")
		print(stock)


def num_in_stock(fruit):
	"""
	This function returns the number of a fruit in stock
	"""
	if fruit == 'apple':
		return 2
	if fruit == 'durian':
		return 4
	if fruit == 'pear':
		return 1000
	else:
		# this is the default case
		return 0


if __name__ == '__main__':
    main()