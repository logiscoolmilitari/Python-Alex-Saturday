my_list = []
a_list_only_with_numbers = []
other_elements = []
length = int(input("How many elements do you want in the list? "))

for i in range(length):
    my_element = input("What's the element? ")
    my_list.append(my_element)
print("Your list is: " + str(my_list)) #adaugat un "+" intre "Your list is: " si my_list (1)
                                        #schimbat my_list cu str(my_list) (4)

########################################################################################################################

for i in range(len(my_list)):  #schimbat my_list cu len(my_list) (5)
    if my_list[i].isdigit(): # schimbat my_list(i) cu my_list[i] (7)
        a_list_only_with_numbers.append(int(my_list[i])) # schimbat a_list_only_with_numbers = append(int(my_list[i])) cu  a_list_only_with_numbers.append(int(my_list[i])) (8)
    else:
        other_elements.append(my_list[i])
print("The list only with numbers from my_list: ", a_list_only_with_numbers)
print("Other elements from my_list: ", other_elements)

########################################################################################################################

i = 0
sum_without_the_max_number = 0
maxim = -9999

for i in range(len(a_list_only_with_numbers)): # schimbat while i < len(a_list_only_with_numbers): cu for i in range(len(a_list_only_with_numbers)): (9)
    if maxim < a_list_only_with_numbers[i]:
        maxim = a_list_only_with_numbers[i] #schimbat maxim == cu maxim = (10)
    sum_without_the_max_number += a_list_only_with_numbers[i]
    i -= 1
sum_without_the_max_number -= maxim
print("The max element is: ", maxim)
print("Sum of the list's elements without the max element: ", sum_without_the_max_number)

########################################################################################################################


def compare(a, b):
    return (a < b) - (a > b)


def sort_string(arr):
    temp = 0 #schimbat temp = "" cu temp = 0 (6)
    for k in range(len(arr) - 1):
        for j in range(k + 1, len(arr)): #adaugat "," intre 1 si len(arr) (3)
            if compare(arr[j], arr[k]) > 0:
                temp = arr[j]
                arr[j] = arr[k]
                arr[k] = temp
    return arr


print("The other_list sorted that contains the strings elements from my_list: ", sort_string(other_elements))

########################################################################################################################

"""!!! The magic secret is here. If you will fix the code, you can take the secret !!!"""

secret = 'LOGI{Here_you_are_master_of_python: 4}'
print("Your flag is here: ", secret)





