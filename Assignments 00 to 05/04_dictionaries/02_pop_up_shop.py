#           **04_dictionaries**

# 02_pop_up_shop
def pop_up_shop():
    fruits = {'durian': 50, 'jackfruit': 80, 'rambutan': 1.5, 'mango': 5, 'apple': 1.5, 'kiwi': 1,}
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input("How many (" + fruit_name + ") do you want to buy?: "))
        total_cost += (price * amount_bought)
    
    print("Your total is $" + str(total_cost))


# Call the main function

if __name__ == '__main__':
    pop_up_shop()