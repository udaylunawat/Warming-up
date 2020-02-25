# https://practice.geeksforgeeks.org/problems/operating-an-array/1#ExpectOP

# Your task is to complete all
# three functions

# if the element is found in the list
# function  must return true or else
# return false
def searchEle(a, x):
    if x in a: return True; return False

# fucntion must return true if 
# insertion is successful or else
# return false
def insertEle(a, y, yi):
    a.insert(yi, y)
    return True

# fucntion must return true if 
# deletion is successful or else
# return false
def deleteEle(a, z):
    while z in a:
        a.remove(z)
    return True