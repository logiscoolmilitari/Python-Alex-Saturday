my_list = []
a_list_only_with_numbers = []
other_elements = []
length = int(input("How many elements do you want in the list? "))  #am pus functia "int" ca sa transform stringul in nr


for i in range(length):
    my_element = input("What's the element? ")
    my_list.append(my_element)
print("Your list is: ", my_list)

########################################################################################################################

for i in range(len(my_list)): #am mai adaugat "len" prntru parcurgerea listei
    if my_list[i].isdigit():
        a_list_only_with_numbers.append(int(my_list[i])) #am transformat elemente din lista care sunt numere in inturi
    else:
        other_elements.append(my_list[i]) #am modificat paranteza de la "i" din rotunda in patrata
print("The list only with numbers from my_list: ", a_list_only_with_numbers)
print("Other elements from my_list: ", other_elements)

########################################################################################################################

i = 0
sum_without_the_max_number = 0 #am sters ghilimelele de la zero
maxim = -9999

while i < len(a_list_only_with_numbers):
    if maxim < a_list_only_with_numbers[i]:
        maxim = a_list_only_with_numbers[i]
    sum_without_the_max_number += a_list_only_with_numbers[i]
    i += 1
sum_without_the_max_number -= maxim #am schimbat din '=-' in '-='
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


print("The other_list sorted that contains the strings elements from my_list: ", sort_string(other_elements)) #am schimbat parantezele patrate cu cele rotunde

########################################################################################################################

"""!!! The magic secret is here. If you will fix the code, you can take the secret !!!"""

secret = 'LOGI{Here_you_are_master_of_python: 1}'
print("Your flag is here: ", secret)





