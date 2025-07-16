for i in range(4):
    print(i)
#for loop with lists
l = [1,4,6,234,6,764]
for i in l:
    print(i)

#for loop with tuples
t = (6,231,75,122)
for i in t:
    print(i)

#for loop with strings
s = "aastha"
for i in s:
    print(i)


#for loop with else
l = [1,7,8]
for item in l:
    print(item)
else:
    print("done") #this is printed when the loop is exhausted


#break and continue in for loop
for i in range(100):
    if(i == 76):
        break #this will stop the loop when i is 76
    print(i)

for i in range(100):
    if(i == 76):
        continue #this can skip the iteration when i is 76
    print(i)



# pass in python
for i in range(100):
    pass  #

i = 0
while(i<45):
    print(i)
    i +=1
