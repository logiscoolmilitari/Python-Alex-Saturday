items = ["Tomatoes", "Cucumbers", "Red Onion", "Green Onion",
         "Green Salat", "Potatoes", "Cabbage", "Beans", "Cherries", "Strawberries"]
prices = [12.50, 6.50, 8.50, 2.00, 3.00, 4.75, 5.00, 13.60, 50.00, 25.00]


# First task: Complete the function that prints all the items with their prices(hint: items[0] -> prices[0])
def print_items_with_their_prices():
    for i in range(len(items)):
        print(items[i] +" are "+str(prices[i])+" $")


print_items_with_their_prices()

# Second task: Complete the function that gives us the most expensive item
def the_most_expensive_item():
    maxim = -9999
    index = -1
    for i in range(len(items)):
        if maxim < prices[i]:
            maxim = prices[i]
            index = i
    print("most_expensive:" + items[index])



the_most_expensive_item()


# Third task: Complete the function that gives us the cheapest item
def the_cheapest_item():
    maxim = 9999
    index = -1
    for i in range(len(items)):
        if maxim > prices[i]:
            maxim = prices[i]
            index = i
    print("cheapest:"+items[index])


the_cheapest_item()


# Fourth task: Create a new list with items that costs less than 10.00 lei. Print the new list using a while loop!
def shopping():
    shop=[]
    for i in range(len(items)):
        if prices[i] <= 10:
            shop.append(items[i])
            shop.append(prices[i])
    print(shop)



shopping()