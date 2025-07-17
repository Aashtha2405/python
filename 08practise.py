#problem1
a = 1
b = 2
c = 3
def greatest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    
a = 1
b = 2
c = 3

print(greatest(a,b,c))

# problem2
def f_to_c(f):
    return 5*(f-32)/9


f = int(input("enter temperature in f: "))
# c = 5*(f-32)/9
print(f_to_c(f))


#problem3
#new line ko avoid krne ke liye end parameter use hota h
print("a")
print("b")
print("c", end="")
print("d", end="")


#problem4
def sum(n):
    if(n == 1):
        return 1
    return sum(n-1) + n

print(sum(4))