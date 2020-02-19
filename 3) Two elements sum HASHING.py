def element_sum_hashing(A, n, sum):
    # Create an empty hash set
    s = set()
    
    for i in range(0, n):
        temp = sum - A[i]
        if temp in s:
            print("Pair with given sum {} is ({}, {})".format(str(sum), str(A[i]), str(temp)))
        s.update({A[i]})

A = [1, 4, 45, 6, 10, 8] 
n = 16
element_sum_hashing(A, len(A), n)