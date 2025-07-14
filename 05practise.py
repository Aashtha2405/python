#problem1
words = {
    "madad": "help",
    "kutta": "dog",
    "khusi": "happiness"
}
word = input("enter a word you wannt to know meaning of:")
print(words[word])

#problem2
s = set()
n = input("Enter number 1: ")
s.add(int(n))
n = input("Enter number 2: ")
s.add(int(n))
n = input("Enter number 3: ")
s.add(int(n))
n = input("Enter number 4: ")
s.add(int(n))
n = input("Enter number 5: ")
s.add(int(n))
n = input("Enter number 6: ")
s.add(int(n))
n = input("Enter number 7: ")
s.add(int(n))
n = input("Enter number 8: ")
s.add(int(n))
print(s)

#problem3
s = set()
s.add(18)
s.add("20")
s.add(20.0)
print(s)

#problem5
s = {}
print(type(s))

#problem6
d = {}
name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang}) 

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

print(d)
