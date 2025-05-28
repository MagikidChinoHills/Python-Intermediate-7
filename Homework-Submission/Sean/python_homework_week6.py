# prob 1 - name stuff
full_name = "Sean Wu"
print("Hello, my name is " + full_name)  # say hi
print(full_name.split()[0])               # just first name

print("-----")

# prob 2 - string methods
sent = input("say something: ")
print(len(sent))          # how long
print(sent.upper())       # all caps
print(sent.lower())       # all small
print(sent.capitalize())  # first letter big
print(sent.count('a'))    # count a’s
print(sent.endswith('?')) # ends with ?

print("-----")

# prob 3 - date + math
from datetime import datetime
now = datetime.now()
print("date is {}/{}/{}".format(now.day, now.month, now.year))  # today

x=5
y=3
print(f"{x} * {y} = {x*y}")  # math
