#problem1
n = int(input("enter a number: "))

for i in range(1,11):
    print(f"{n} * {i} = {n*i}")

#problem2
l = ["sangita","sanjana","sanjay","sawaliya","aastha","rohail"]

for name in l:
    if name.startswith("s"):
        print(name,"stats with s")

#problem3
n = int(input("enter a number: "))
i = 1
while(i<11):
    print(f"{n} * {i} = {n*i}")
    i +=1

#problem4 print prime number
n = int(input("enter a number: "))
for i in range(2,n):
    if(n%i) == 0:
        print("number is not prime")
        break
else:
    print("number is prime")

#problem5
n = int(input("enter the number: "))
i = 1
sum = 0
while(i<=n):
    sum += i
    i+=1
print(sum)

#problem6 factorial
n = int(input("enter a number: "))
product = 1
for i in range(1, n+1):
    product = product * i
print(f"factorial of {n} is {product}")


#problem7
#star printing by for loop 
