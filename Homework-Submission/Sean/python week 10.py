# Problem 1

# greet user
def greet_user(name):
  print("Hello " + name + "! Welcome!")

# square a number
def square_number(num):
  return num*num


# Problem 2

# get area of rectangle
def calculate_area(length=1, width=1):
  return length * width


# Problem 3

# divide and get quotient + remainder
def divide_numbers(a, b):
  q = a // b
  r = a % b
  return q, r


# Problem 4

# add any numbers
def calculate_sum(*args):
  s = 0
  for n in args:
    s += n
  return s


# Problem 5

# factorial using recursion
def factorial(n):
  if n==0 or n==1:
    return 1
  return n * factorial(n-1)



# calling functions below 

greet_user("Sean")

x = square_number(7)
print("square of 7:", x)

a = calculate_area(5, 3)
print("area is", a)

q, r = divide_numbers(20, 6)
print("quotient is", q)
print("remainder is", r)

sum_result = calculate_sum(5,10,15)
print("sum:", sum_result)

f = factorial(5)
print("factorial:", f)
