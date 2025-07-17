#function and recursion


#funnction definition 
def avg():
    a = int(input("enter your number: "))
    b = int(input("enter your number: "))
    c = int(input("enter your number: "))

    average = (a+b+c)/3
    print(average)

avg() #this is function calling


#quick quiz
#greeting function
def goodday():
    print("goodday")

goodday()
  

def goodday(name, ending):
    print("goodday", name)
    print(ending)

goodday("aastha", "thankyou")
goodday("balag","thanks")


