#recursion is a function which called itself
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("enter a number: "))
print(f"the factorial of number is: {factorial(n)}")
    
