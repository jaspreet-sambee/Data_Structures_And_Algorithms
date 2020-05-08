# Uses python3
def calc_fib_slow(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib(n):
    if (n <= 1):
        return n

    fib_arr = [0] * n
    fib_arr[0] = 0
    fib_arr[1] = 1

    for i in range(2,n):
        fib_arr[i] = fib_arr[i-1] + fib_arr[i-2]

    return (fib_arr[n-1] + fib_arr[n-2])

n = int(input())
print(calc_fib(n))
