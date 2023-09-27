items = ["Tomatoes", "Cucumbers", "Red Onion", "Green Onion",
         "Green Salat", "Potatoes", "Cabbage", "Beans", "Cherries", "Strawberries"]
prices = [12.50, 6.50, 8.50, 2.00, 3.00, 4.75, 5.00, 13.60, 50.00, 25.00]


# First task: Complete the function that prints all the items with their prices(hint: items[0] -> prices[0])
def print_items_with_their_prices():
    for i in range(len(items)):
        print(items[i] + "->" + str(prices[i]))


print_items_with_their_prices()

# Second task: Complete the function that gives us the most expensive item
print("")
def the_most_expensive_item():
    price = 0
    expensive = ""
    for i in range(len(items)):
        if prices[i] > float(price):
            price = prices[i]
            expensive = items[i]
    print("The most expensive item is: " + expensive)



the_most_expensive_item()


# Third task: Complete the function that gives us the cheapest item
print("")
def the_cheapest_item():
    price = 9999999
    cheep = ""
    for i in range(len(items)):
        if prices[i] < float(price):
            price = prices[i]
            cheep = items[i]
    print("The cheapest item is: " + cheep)


the_cheapest_item()


# Fourth task: Create a new list with items that costs less than 10.00 lei. Print the new list using a while loop!
print("")

def shopping():
    shopd = []
    i = 1
    print("Items that cost less that 10 lei:")
    while prices[i] < 10 and i < len(prices):
        shopd.append(items[i])
        i += 1
    print(shopd)


shopping()