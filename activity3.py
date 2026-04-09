def factorial(x):
    '''this is a recursive function to find the factorial of an integer'''
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
print(factorial.__doc__)
print("the factorial of 0:",factorial(0))
print("the factorial of 1:",factorial(1))
print("the factorial of 2:",factorial(2))
print("the factorial of 5:",factorial(5))
print("the factorial of 10:",factorial(10))
print("the factorial of 954:",factorial(954))
print("the factorial of 25:",factorial(25))
print("the factorial of 23:",factorial(23))
print("the factorial of 34:",factorial(34))
print("the factorial of 27:",factorial(27))
print("the factorial of 2925:",factorial(2925))
print("the factorial of 12984:",factorial(12984))