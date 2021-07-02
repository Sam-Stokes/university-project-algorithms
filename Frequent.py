# Author : Sam Stokes
# Date : November 2020
"""
This program finds the most frequent word in an array.
If multiple words have same frequency, the word whose first occurrence occurs last in the array
is printed, as compared to the other strings with same frequency
"""


def most_frequent(a1):
    count = 0
    word = a1[0]

    for i in a1:
        curr_freq = a1.count(i)
        if curr_freq >= count:
            count = curr_freq
            word = i

    return word


arr = []
n = int(input("Enter number of elements in the list: "))  # We define the number of elements to be added

# For loop for adding the elements to the empty array
for j in range(0, n):
    print("Enter Element {}: ".format(j + 1))  # The format function used for place holders
    elm = (input())  # The input function used to store the element in the variable
    arr.append(elm)  # The element will be added to the array

print('The most frequent word is: ', most_frequent(arr))

