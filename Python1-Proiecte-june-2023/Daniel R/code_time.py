items = ["Tomatoes", "Cucumbers", "Red Onion", "Green Onion",
         "Green Salad", "Potatoes", "Cabbage", "Beans", "Cherries", "Strawberries"]
prices = [12.50, 6.50, 8.50, 2.00, 3.00, 4.75, 5.00, 13.60, 50.00, 25.00]


# First task: Complete the function that prints all the items with their prices(hint: items[0] -> prices[0])
def print_items_with_their_prices():
    for i in range(len(items)):
        print("The " + items[i] + " costs " + str(prices[i]) + " lei!")



print_items_with_their_prices()

# Second task: Complete the function that gives us the most expensive item
def the_most_expensive_item():
    maxim = -9999
    index = -1
    for i in range(len(prices)):
        if maxim < prices[i]:
            maxim = prices[i]
            index = i
    print("The most expensive item is " + items[index] + " and costs " + str(maxim) + " lei!")


the_most_expensive_item()


# Third task: Complete the function that gives us the cheapest item
def the_cheapest_item():
    minim = +9999
    index = +1
    for i in range(len(prices)):
        if minim > prices[i]:
            minim = prices[i]
            index = i
    print("The most cheapest item is " + items[index] + " and costs " + str(minim) + " lei!")



the_cheapest_item()


# Fourth task: Create a new list with items that costs less than 10.00 lei. Print the new list using a while loop!
def shopping():
    shopping_list = []
    for i in range(len(prices)):
        if 10 > prices[i]:
            shopping_list.append(items[i])
    i = 0
    print("The shopping list contains: ", end="")
    while i < len(prices):
        print(shopping_list[i], end=",")
        i += 1


shopping()