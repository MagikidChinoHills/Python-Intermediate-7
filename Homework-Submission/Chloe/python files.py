full_name = "Sean Wu"
greeting = "Hello, my name is " + full_name
print(greeting)

first_name = full_name[:full_name.find(" ")]
print("First name:", first_name)

sentence = input("Enter a sentence: ")
print("Length of sentence:", len(sentence))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Capitalized:", sentence.capitalize())
letter_to_count = 'e'
print(f"Occurrences of '{letter_to_count}':", sentence.count(letter_to_count))
print("Ends with question mark?", sentence.endswith("?"))

day = 10
month = 5
year = 2025
formatted_message = "Today's date is {}/{}/{}".format(month, day, year)
print(formatted_message)

a = 5
b = 3
result = a * b
print(f"The result of {a} multiplied by {b} is {result}.")
