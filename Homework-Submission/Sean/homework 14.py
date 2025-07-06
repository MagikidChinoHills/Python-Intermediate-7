f = open("input.txt", "r")#opens input.txt 
print(f.read())#reads what is in it
f.close()#closes file

with open("output.txt", "a") as f:#opens file
    f.write("this text will be added to the end of the file.\n")#adds text
f.close()#closes file

f=open("data.csv","r")
print(f.read())
f.close()

import json

data = {"name": "Sean Wu", "age": 10}

with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json") as f:
    print(json.load(f))
