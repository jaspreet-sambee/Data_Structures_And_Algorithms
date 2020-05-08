# Uses python3
import sys

def lcm_naive_orig(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_naive(a, b):
    if b == 0:
        return a
    rem = (a%b)

    return gcd_naive(b,rem)

def lcm_naive(a, b):


    return (a*b)//gcd_naive(a,b)

if __name__ == '__main__':
    #input = sys.stdin.read()
    a, b = map(int, input().split())
    print(lcm_naive(a, b))

