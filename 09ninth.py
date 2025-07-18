#file input/output

f = open("fiile.txt")
data = f.read()
print(data)
f.close()

st = "aastha is best"

f = open("myfile.txt","w")
f.write(st)
f.close()