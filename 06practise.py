# quick quiz
a = int(input("Enter your age: "))
if(a>18):
    print("you are adult")
else:
    print("you are not adult")

#problem1
a1 = int(input("enter number 1: "))
a2 = int(input("enter number 2: "))
a3 = int(input("enter number 3: "))
a4 = int(input("enter number 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("a1 is greatest number",a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("a2 is greatest number", a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("a3 is greatest number", a3)

elif(a4>a1 and a4>a2 and a4>a3):
    print("a4 is greatest number", a4)
    
#problem2
marks1 = int(input("enter marks 1: "))
marks2 = int(input("enter marks 2: "))
marks3 = int(input("enter marks 3: "))

#check for total peracentage
total_percentage = (100*(marks1+marks2+marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("pass",total_percentage)
else:
    print("better luck next time",total_percentage)

#problem3
p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"
message = input("enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this is spam")
else:
    print("this is not spam")

#problem4
username = input("enter username: ")
if(len(username)<10):
   print("your username contains less than 10 character")
else:
   print("your username contains more than 10 character")

#problem5
l = ["jaya","vijaya","aastha","laxmi"]
name = input("enter your name: ")
if(name in l):
    print("your name is the list")
else:
    print("your name is not the list")

#problem6
marks = int(input("enter your marks: "))

if(marks<=100 and marks>=90):
    grade = "ex"
elif(marks<90 and marks>=80):
    grade = "a"
elif(marks<80 and marks>=70):
    grade = "b"
elif(marks<70 and marks>=60):
    grade = "c"
elif(marks<60 and marks>=50):
    grade = "d"
elif(marks<50):
    grade = "f"


print("your grade is:",grade)

#problem7
post = input("enter the post: ")
if("harry" in post):
    print("this post is talking about harry")
else:
    print(" this post is not talking about harry")