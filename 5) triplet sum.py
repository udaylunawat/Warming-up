'''
https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/

Given an array and a value, find if there is a triplet in array 
whose sum is equal to the given value. If there is such a triplet present in array, 
then print the triplet and return true. Else return false. 
For example, if the given array is {12, 3, 4, 1, 6, 9} and given sum is 24, 
then there is a triplet (12, 3 and 9) present in array whose sum is 24.
'''

def triplet_sum(array, n, sum):
    array.sort()
    start = 0
    end = n-1

    while start<end:
        if array[start]+array[end] < sum:
            for i in range(0, end):
                if i == start:
                    continue
                elif array[start] + array[end] + array[i] == sum:
                    print("{} + {} + {} = {}".format(array[start], array[end], array[i], sum))
                    return True
            start += 1
        elif array[start]+array[end] > sum:
            end -= 1
    return False


a = [12, 3, 4, 1, 6, 9]
s = 24
triplet_sum(a, len(a), s)

