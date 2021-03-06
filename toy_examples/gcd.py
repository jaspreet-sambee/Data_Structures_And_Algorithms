# Uses python3
import sys

def gcd_naive_orig(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_naive(a, b):
    if b == 0:
        return a
    rem = (a%b)

    return gcd_naive(b,rem)

if __name__ == "__main__":
    #input = sys.stdin.read()
    input = input()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))

