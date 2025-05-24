person = {
    'Name': 'Alice',
    'Age': 30,
    'City': 'New York',
    'Occupation': 'Engineer'
}

print("Entire dictionary:")
print(person)

print("\nIndividual Information:")
print("Name:", person['Name'])
print("Age:", person['Age'])
print("City:", person['City'])
print("Occupation:", person['Occupation'])

person['City'] = 'San Francisco'
print("\nModified Dictionary (City changed):")
print(person)

inventory = {
    'apples': 10,
    'bananas': 5,
    'oranges': 8
}

inventory['grapes'] = 15
print("\nInventory after adding grapes:")
print(inventory)

del inventory['bananas']
print("\nInventory after removing bananas:")
print(inventory)

inventory['apples'] = 20
print("\nInventory after updating apples quantity:")
print(inventory)

item_to_check = 'oranges'
if item_to_check in inventory:
    print(f"\n{item_to_check} are in the inventory.")
else:
    print(f"\n{item_to_check} are NOT in the inventory.")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("\nSet 1:", set1)
print("Set 2:", set2)
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)

number_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_numbers = list(set(number_list))
print("\nOriginal List:", number_list)
print("List after removing duplicates:", unique_numbers)
