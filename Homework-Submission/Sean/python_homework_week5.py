# --- Problem 1: List stuff ---
# A list is mutable — you can add, change, or remove stuff.

nums = [1, 2, 3, 4, 5]      # a list of numbers

nums.append(6)             # add 6 to the end
nums.append(7)             # add 7 too
nums.remove(3)             # remove the number 3

# Indexing: get item by position (starts from 0)
print(nums[0])             # print first item
nums[0] = 10               # change first item to 10
print(nums[0])             # print it again

print(nums)                # final version of the list

print("--------")

# --- Problem 2: Tuple stuff ---
# A tuple is immutable — you can’t change it once it’s made.

fruits = ("apple", "banana", "cherry")  # a tuple of fruits

print(fruits[0])            # print first fruit

# Trying to change a tuple will cause an error
try:
    fruits[1] = "blueberry"  # tuples can't be changed!
except TypeError as e:
    print("nah:", e)

# We can still create new tuples by combining them
more = ("orange", "grape")
all_fruits = fruits + more  # combine tuples

print(fruits)               # original tuple
print(all_fruits)           # new combined one

print("--------")

# --- Problem 3: Essay thing (explaining key concepts) ---
essay = """
LISTS:
- Lists are MUTABLE → you can change, add, or remove items.
- Use when your data will change.
- Example: [1, 2, 3]

TUPLES:
- Tuples are IMMUTABLE → you can't change them after creation.
- Good for fixed data you don’t want accidentally modified.
- Example: (1, 2, 3)

INDEXING:
- Both lists and tuples use indexing to get items.
- Indexes start at 0. my_list[0] gives the first item.
- Negative indexes work too. my_list[-1] is the last item.

MUTABILITY vs IMMUTABILITY:
- MUTABLE = can be changed (like lists, dictionaries).
- IMMUTABLE = can’t be changed (like tuples, strings).
- Immutability helps keep data safe and consistent.
- Only immutable types can be used as dictionary keys.

WHEN TO USE WHAT:
- Use lists when your data changes often.
- Use tuples when the data should stay the same.
- Tuples are slightly faster and safer for fixed data.
"""

print(essay)
