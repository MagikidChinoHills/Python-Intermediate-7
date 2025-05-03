# List example
my_list = ["a", "b", "c"]
print(my_list[1])
my_list[1] = "z"
print(my_list)

# Tuple example
my_tuple = ("x", "y", "z")
print(my_tuple[2])
try:
    my_tuple[1] = "q"
except TypeError as e:
    print(e)

# More list changes
numbers = [1, 2, 3]
numbers.append(4)
numbers.remove(2)
numbers[1] = 10
print(numbers)

# Tuple combining
animals = ("cat", "dog", "fish")
print(animals[0])
try:
    animals[0] = "hamster"
except TypeError as e:
    print(e)

more_animals = ("lion", "tiger")
all_animals = animals + more_animals
print(all_animals)
