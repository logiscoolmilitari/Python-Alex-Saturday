my_list = [] #am modificat parantezele rotunde in paranteze patrate
a_list_only_with_numbers = []
other_elements = []
length = int(input("How many elements do you want in the list? "))

for i in range(length):
    my_element = input("What's the element? ")
    my_list.append(my_element) #am modificat = in .
print("Your list is: ", my_list)

########################################################################################################################

for i in range(len(my_list)):
    if my_list[i].isdigit():
        a_list_only_with_numbers.append(int(my_list[i])) #am transformat din string in numar folosind int
    else:
        other_elements.append(my_list[i])
print("The list only with numbers from my_list: ", a_list_only_with_numbers)
print("Other elements from my_list: ",  other_elements) #am pus o virgula intre str si other elements si am scos parantezele de la other elements

########################################################################################################################

i = 0
sum_without_the_max_number = 0
maxim = -9999 #am schimbat valoarea dintr-un string in numar

while i < len(a_list_only_with_numbers):
    if maxim < a_list_only_with_numbers[i]:
        maxim = a_list_only_with_numbers[i]
    sum_without_the_max_number += a_list_only_with_numbers[i]
    i += 1
sum_without_the_max_number -= maxim
print("The max element is: ", maxim)
print("Sum of the list's elements without the max element: ", sum_without_the_max_number)

########################################################################################################################


def compare(a, b):
    return (a < b) - (a > b)


def sort_string(arr):
    temp = ""
    for k in range(len(arr) - 1):
        for j in range(k + 1, len(arr)):
            if compare(arr[j], arr[k]) > 0:
                temp = arr[j]
                arr[j] = arr[k]
                arr[k] = temp
    return arr


print("The other_list sorted that contains the strings elements from my_list: ", sort_string(other_elements))

########################################################################################################################

"""!!! The magic secret is here. If you will fix the code, you can take the secret !!!"""

secret = 'LOGI{Here_you_are_master_of_python: 2}'
print("Your flag is here: ", secret)





