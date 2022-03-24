""" The example sequence 011212201220200112 ... is constructed as follows: 
1. The first element in the sequence is 0. 
2. For each iteration, repeat the following action: take a copy of the entire current sequence, replace 0 with 1, 1 with 2, and 2 with 0, and place it at the end of the current sequence. E.g. 
0 -> 01 -> 0112 -> 01121220 -> ... 
Create an algorithm which determines what number is at the Nth position in the sequence (using 0-based indexing). """
import math
def find_digit(n):
    start = 0
    while int(n):
        start += 1
        #length = n.bit_length()
        length = math.floor(math.log2(n))
        n -= 2 ** (length - 1)
        print("End", start, length, n)
    return start % 3

print(find_digit(25684))