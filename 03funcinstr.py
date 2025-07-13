name = "Harry"
print(len(name))
print(name.endswith("rry"))
print(name.endswith("rrya"))
print(name.startswith("Ha"))
print(name.capitalize()) #only first letter

#escape sequence character
a = "hello\nworld" #\n is a new line
print(a)

b = "i am good girl \"best\" "
print(b)

#problem1
name = input("Enter your name:")
print(f"good afternoon, {name}")

#problem2
letter = '''Dear <|Name|>,
          you are selected!
<|date|>'''
print(letter.replace("<|Name|>", "Aastha").replace("<|date|>", "1st feb 2028"))
 

#problem3
name = "aastha is  a  good  girl"
print(name.find(" "))

#problem4
name = "aastha is a good girl"
print(name.replace("  "," "))
print(name)

#problem5
letter = "Hi \n Aastha \n\tHow are you"
print(letter)

