# Given an array A[] and a number x, check for pair in A[] with sum as x
# Write a program that, given an array A[] of n numbers and another number x, determines whether or not there exist two elements in S whose sum is exactly x.



def check_sum(array, size_of_array, sum):
    array.sort()
    l = 0
    r = size_of_array - 1

    while l<r:
        if array[l]+array[r] == sum:
            return 1
        elif array[l]+array[r] < sum:
            l+=1
        else:
            r-=1
    return 0

sum = 12
a = [-10,11,8,6,4,2]

if (check_sum(a, len(a), sum)): 
    print("Array has two elements with the given sum") 
else: 
    print("Array doesn't have two elements with the given sum") 