
 # Uses python3
import sys

def get_fibonacci_last_digit_naive_orig(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit_naive(n):
    if (n <= 1):
        return n

    fib_arr = [0] * n
    fib_arr[0] = 0
    fib_arr[1] = 1

    for i in range(2,n):
        fib_arr[i] = ((fib_arr[i-1] + fib_arr[i-2])%10)

    x = (fib_arr[n-1] + fib_arr[n-2])

    if x%10 != x:
        return x%10
    else:
        return (fib_arr[n-1] + fib_arr[n-2])

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
