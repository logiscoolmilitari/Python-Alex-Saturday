items = ["Tomatoes", "Cucumbers", "Red Onion", "Green Onion",
         "Green Salat", "Potatoes", "Cabbage", "Beans", "Cherries", "Strawberries"]
prices = [12.50, 6.50, 8.50, 2.00, 3.00, 4.75, 5.00, 13.60, 50.00, 25.00]


# First task: Complete the function that prints all the items with their prices(hint: items[0] -> prices[0])
def print_items_with_their_prices():
    for i in range(len(items)):
        print(str(items[i]) + " " + str(prices[i]))


print_items_with_their_prices()

# Second task: Complete the function that gives us the most expensive item
def the_most_expensive_item():
    maxim = -9999
    index = -1
    for i in range(len(prices)):
        if prices[i] > maxim:
            maxim = prices[i]
            index = i
    print("the most expensive item is " + items[index])





the_most_expensive_item()


# Third task: Complete the function that gives us the cheapest item
def the_cheapest_item():
    minim = 9999
    index = -1
    for i in range(len(prices)):
        if prices[i] < minim:
            minim = prices[i]
            index = i
    print("the cheapest is " + items[index])


the_cheapest_item()


# Fourth task: Create a new list with items that costs less than 10.00 lei. Print the new list using a while loop!
def shopping():
    lista = []
    for i in range(len(prices)):
        if prices[i] < 10:
            lista.append(items[i])

    print("The items that cost less than 10.00 lei are: ", end="")
    j = 0
    while j < len(lista):
        print(lista[j], end=",")
        j += 1





shopping()