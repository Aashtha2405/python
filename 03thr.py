#intro to string in python
name = "aastha" #double quoted string
name = 'jaya' #single quoted string
name = '''laxmi''' #triple quoted string

name = "ram"
nameshort = name[0:3]
print(nameshort)
character1 = name[1]
print(character1)
character0 = name[0]
print(character0)


#negative slicing
name = "harry"
print(name[0:3])
print(name[-4:-1])
print(name[1:4])
print(name[:4]) #is same as name[0:4]
print(name[1:]) #is same as name[1:5]

#slicing with skip value
word = "amazon"
word[1:6:2]
print(word[1:6:2])


