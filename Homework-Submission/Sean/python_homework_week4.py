number = int(input("Enter an integer: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age entered. Please enter a non-negative number.")
elif age <= 12:
    print("You are a Child.")  
elif age <= 19:
    print("You are a Teenager. You now have the right to vote!")

elif age <= 59:
    print("You are an Adult.")
else:
    print("You are a Senior.")
