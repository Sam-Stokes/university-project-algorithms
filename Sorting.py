# Author : Sam Stokes
# Date : November 2020
"""
This program sorts a list via user input by it's
length (in ascending order) and prints out the result.
"""

list1 = []  # Empty list for the array of user input strings
n = int(input("Enter number of elements in the list: "))  # We define the number of elements to be added

# For loop for adding the elements to the empty array
for i in range(0, n):
    print("Enter Element {}: ".format(i + 1))  # The format function used for place holders
    elm = (input())  # The input function used to store the element in the variable
    list1.append(elm)  # The element will be added to the array

n = len(list1)  # Defining the number of elements in the list
number_of_steps = 0  # Initializing the number of steps taken variable as 0

# Sort using selection sort algorithm
for i in range(n - 1):
    smallest = i
    for j in range(i + 1, n):
        if len(list1[j]) < len(list1[smallest]):
            smallest = j
    list1[i], list1[smallest] = list1[smallest], list1[i]
    number_of_steps += 1

print("The ordered list is:")
print(list1)
print("The list had " + str(n) + " cities and I ordered it in " + str(number_of_steps) + " steps .")