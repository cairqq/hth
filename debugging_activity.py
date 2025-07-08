# Debugging activity - carina bui 

# 1
x = 10
y = 0
if y != 0:
    result = x / y
    print("Result:", result)
else: 
    print("cant divide by zero")
# zero division error cant divide by 0

#2
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[i])
 # index error: the loop was out of range

#3 
def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area

radius = 5
print(calculate_area(radius))
 #syntax error: missing colon

#4
def is_even(number):
   if number % 2 == 0:
       return True
   else:
       return False

print(is_even(4))
print(is_even(7))
 #syntax error: missing colons

#5
for i in range(5):
   print(i)
 #syntax error: missing colon

#6
def greet(name):
   return "Hello, " + name
 
print(greet("Alice"))
 #syntax error: no + to add the string

#7
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
print("Sum of numbers:", sum)
# indentation error

#8
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)
 
print(factorial(5))
#correct no errors


#9
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
   print("Hello, " + name)
else:
   print("Hello, stranger!")

# needed to add name == after or

#10
def divide_numbers(x, y):
    if y == 0:
        return "cant divide by zero"
        return x/y
num1 = 10
num2 = 0
print(divide_numbers(num1, num2))

