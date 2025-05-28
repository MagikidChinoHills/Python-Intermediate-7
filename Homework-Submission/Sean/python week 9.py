#Problem 1
numbers=[3,7,3,9,2,5,2,8,8]  # original list
print("Original numbers:",numbers)

squares=[x**2 for x in numbers]  # square each num
print("Squared numbers:",squares)

evens=[x for x in numbers if x%2==0]  # filter evens only
print("Even numbers:",evens)

desc_nums=numbers[:]  # copy list so original stays
for i in range(len(desc_nums)):
 for j in range(i+1,len(desc_nums)):
  if desc_nums[i]<desc_nums[j]:
   desc_nums[i],desc_nums[j]=desc_nums[j],desc_nums[i]  # swap if smaller
print("Sorted (high to low):",desc_nums)

unique_nums=[]  # to keep unique in order
seen=set()  # track seen nums
for n in numbers:
 if n not in seen:
  unique_nums.append(n)
  seen.add(n)
print("No duplicates:",unique_nums)

# Problem 2
rgb=(123,45,67)  # rgb tuple
print("RGB color:",rgb)

length=0
total=0
for v in rgb:
 length+=1   # count how many
 total+=v    # sum them up
average=total/length  # calc average

print("Length:",length)
print("Sum of values:",total)
print("Average value:",average)

hex_color="#{:02X}{:02X}{:02X}".format(*rgb)  # convert to hex string
print("Hex color code:",hex_color)

#Problem 3       IDK the populations of these cities
cities={"LA":999999,"Chino Hills":1500000,"Mapleton":500000}

cities["Redstone"]=1200000  # add new city
cities.pop("Mapleton")        # remove tinyville
cities["Chino Hills"]=2000000      # update bigcity pop

print("Updated city data:",cities)

large={}  # dict for big cities
for c,p in cities.items():
 if p>1000000:  # only cities with pop>1M
  large[c]=p
print("Cities with over 1 million people:",large)

# --- Problem 4: Playing with Sets ---
a={1,2,3,4}
b={3,4,5,6}

print("Is A a subset of B?",a<=b)  # check subset
print("Union of A and B:",a|b)     # union of sets
print("Intersection of A and B:",a&b)  # common elems
print("Difference (A - B):",a-b)        # what’s in a not b

words=["apple","banana","apple","grape","banana"]  # list with dups
unique_words=list(set(words))  # set removes dups, list back

print("Original words:",words)
print("Without duplicates:",unique_words)
