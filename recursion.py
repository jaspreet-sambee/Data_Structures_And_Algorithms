#Recursive Function to keep on adding until n gets to 1
def sum_to_one(n):
  if n == 1:
    return n
  else:
    print("Recursing with input: {0}".format(n))
    return sum_to_one(n-1) + n

# uncomment when you're ready to test
#print(sum_to_one(7))

def factorial(n):
  if n == 1:
    return n
  else:
    print("Recursing with input: {0}".format(n))
    return factorial(n-1) *n

#print(factorial(1234))  --> will reach recursion depth

#--> Recursion can be slightly worse than iterative solutions because of the call stack

def flatten(my_list):
  result = []
  for el in my_list:
    if isinstance(el, list):
      print("list found!")
      flat_list = flatten(el)
      result += flat_list
    else:
      result.append(el)
  return result


### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))

def fibonacci(n):
  if n==1:
    return 1
  elif n==0:
    return 0
  else:
    print("values:",n)
    return fibonacci(n-2) + fibonacci(n-1)



print(fibonacci(5))
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"
