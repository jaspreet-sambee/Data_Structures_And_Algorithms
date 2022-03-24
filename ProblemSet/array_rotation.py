#This file contains problems relevant to array rotation

# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements. (https://www.geeksforgeeks.org/array-rotation/)
def rotate(arr, d, n):  #O(n) and O(n)
    print(arr)
    temp = arr.copy()
    for i in range(n):
      if i < d:
        arr[n-d+i] = temp[i]
      else:
        arr[i-d] = temp[i]
    return arr

def reverse_array(arr, start, end):
    #for i in range(d):
    while(start < end):
      temp = arr[start]
      arr[start] = arr[end]
      arr[end] = temp
      start += 1
      end -= 1

def reversal_rotate(arr, d, n):
    if d==0:
        return
    #if d > n
    d = d%n
    reverse_array(arr, 0, d-1)
    reverse_array(arr, d, n-1)
    reverse_array(arr, 0, n-1)
    return arr
print(rotate([2,3,4,5,6], 2, 5))
print(reversal_rotate([3,4,5,6,7,8], 2, 6))