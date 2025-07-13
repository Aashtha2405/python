#list are containers to stores a set of value of any data types ex- 
friend = ["apple","banana","cherry","aastha",False, 34.5,45]
print(friend[0]) #accessing first elemeent

friend[0] = "mango" #changing the first element
print(friend[0]) #accesing first elememt after change

#different method in list
friend = ["apple","banana","cherry","aastha",False, 34.5,45]
friend.append("mango") #adding an element at the end
print(friend)

l1 = [1,4,7,8,9]
l1.reverse()
print(l1)
l1.sort()
l1.insert(2,5) #inserting 5 at index 2
l1.pop(3)
print(l1)
value = l1.pop(2) #removing the element at index  2
print(value)

# #Tuples 
a = (1,2,3,4,5)
print(type(a))
b = ()
print(type(b))
a = (1)
print(type(a))
#yha int de tuple nhi so now 
a = (1,)
print(type(a))
#tuple ke elements ko change nhi kr skte h



#method of tuple
a = (1,45,342,3424,False,46,"aastha")
print(a)
no = a.count(45)
print(no)








