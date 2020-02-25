"""
https://www.geeksforgeeks.org/two-pointers-technique/
Two Pointers Technique
Two pointers is really an easy and effective technique which is typically used for searching pairs in a sorted array.

Given a sorted array A (sorted in ascending order), having N integers, 
find if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X.

The below solution works in O(n)

How does this work?
The algorithm basically uses the fact that the input array is sorted. 
We start the sum of extreme values (smallest and largest) and conditionally move both pointers. 
We move left pointer i when the sum of A[i] and A[j] is less than X. 
We do not miss any pair because the sum is already smaller than X. Same logic applies for right pointer j.
"""

def two_pointers(array, size_of_array, sum):
    array.sort()
    l = 0
    r = size_of_array - 1

    while l<r:
        if array[l]+array[r] == sum:
            print("{} + {} = {}".format(array[l], array[r], sum))
            return True, array[l], array[r]
        elif array[l]+array[r] < sum:
            l+=1
        else:
            r-=1
    return False

sum = 12
a = [-10,11,8,6,4,2]
if (two_pointers(a, len(a), sum)): 
    print("Array has two elements with the given sum") 
    print()
else: 
    print("Array doesn't have two elements with the given sum") 