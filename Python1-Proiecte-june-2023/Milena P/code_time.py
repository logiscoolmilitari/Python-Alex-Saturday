items = ["Tomatoes", "Cucumbers", "Red Onion", "Green Onion",
         "Green Salat", "Potatoes", "Cabbage", "Beans", "Cherries", "Strawberries"]
prices = [12.50, 6.50, 8.50, 2.00, 3.00, 4.75, 5.00, 13.60, 50.00, 25.00]


# First task: Complete the function that prints all the items with their prices(hint: items[0] -> prices[0])
def print_items_with_their_prices():
    for i in range (len(items)):
        print('The '+ items[i] + ' costs ' + str(prices[i]))
print(print_items_with_their_prices)


print_items_with_their_prices()

# Second task: Complete the function that gives us the most expensive item
def the_most_expensive_item():
    maxim = -999
    index = -1
    for i in range (len(prices)):
        if maxim < prices[i]:
            maxim = prices[i]
            index = i
    print("This is the most expensive item" + items[index] + " and it costs " + str(maxim))



the_most_expensive_item()


# Third task: Complete the function that gives us the cheapest item
def the_cheapest_item():
        minim = 999
        index = -1
        for i in range(len(prices)):
            if minim > prices[i]:
                minim = prices[i]
                index = i
        print("This is the most cheapest item" + items[index] + " and it costs " + str(minim))


the_cheapest_item()


# Fourth task: Create a new list with items that costs less than 10.00 lei. Print the new list using a while loop!
def shopping():
    items_2 = []
    index = 0
    for i in range (len(prices)):
        if prices[i] < 10:
            items_2.append(items[i])
    print("Produsele mai ieftine de 10 lei: ", end="")
    while index < (len(items_2)):
        print(items_2[index],end=",")
        index += 1


shopping()