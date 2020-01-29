# Search operation using Binary search
# Search: O(Log n) [Using Binary Search]
# Insert: O(n) [In worst case all elements may have to be moved]
# Delete: O(n) [In worst case all elements may have to be moved]

def binarySearch(arr, low, high, key):
    if high < low:
        return -1
    
    mid = low + (high - low)/2
    # https://www.geeksforgeeks.org/start-end-start2-preferrable-method-calculating-middle-array-start-end2/amp/
    # mid = (low + high)/2

    if key == arr[int(mid)]:
        return mid

    elif key > mid:
        return binarySearch(arr, mid+1, high, key)

    else:
        return binarySearch(arr, low, mid-1, key)

#Insert operation

def insertSorted(array, pos, key, capacity):
    if pos >= capacity:
        return pos
    
    i = n-1
    while i >= 0 and arr[i] > key: 
        arr[i + 1] = arr[i] 
        i -= 1

    arr[i+1] = key
    return (n + 1)

def deleteElement(arr, n, key):
    index = binarySearch(arr, 0, n-1, key)

    if index == -1:
        return n
    
    #Shifting elements larger elements to the left
    for i in range(int(index),n-1):
        arr[i] = arr[i+1]

    return n-1





# Driver program to check above functions  
# Let us search 3 in below array 
arr = [5, 6, 7, 8, 9, 10] 
n = len(arr) 
key = 10
print("Index:", int(binarySearch(arr, 0, n, key) )) 



for i in range(20): 
    arr.append(0) 
  
capacity = len(arr) 
n = 6
key = 26
  
print("Before Insertion: ", end = " "); 
for i in range(n): 
    print(arr[i], end = " ") 
      
# Inserting key 
n = insertSorted(arr, n, key, capacity) 
  
print("\nAfter Insertion: ", end = "") 
for i in range(n): 
    print(arr[i], end = " ") 



print("\nBefore Deletion: ", end = " "); 
for i in range(n): 
    print(arr[i], end = " ") 
      
# Deleting key
key = 26 
n = deleteElement(arr, n, key) 
  
print("\nAfter Deletion: ", end = "") 
for i in range(n): 
    print(arr[i], end = " ") 