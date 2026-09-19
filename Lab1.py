# Lab 1
# Introduction to Python

print("Hello, World!")

# Input and Output
name = input("Enter your name: ")
print("Welcome", name)

# Multiple statements
x = 10
y = 20

print("x =", x)
print("y =", y)

# Indentation
if x < y:
    print("x is smaller than y")

# Data Types
a = 25
b = 8.75
c = 3 + 4j
d = True
text = "Python"

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(text, type(text))

# Type Casting
num = "50"

print("Before conversion:", num, type(num))

num = int(num)

print("After conversion:", num, type(num))

num2 = float(num)

print("Float value:", num2, type(num2))

# Numbers
a = 12
b = 5

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Integer Division =", a // b)
print("Remainder =", a % b)
print("Power =", a ** b)

# Boolean
result = a > b

print(result)
print(type(result))

# Strings
text = "PYTHON TUTORIAL"

print(text)

print("First character:", text[0])
print("Last character:", text[-1])
print("Character at index 3:", text[3])

# Escape characters
print("Hello\nPython")
print("Hello\tPython")
print("C:\\Python\\Lab")
print("It's Python")
print("\"Python Lab\"")

# String Slicing
print(text[0:6])
print(text[7:])
print(text[-8:])

# Lists
colors = ["RED", "Blue", "Green", "Black"]

print(colors)

print("First item:", colors[0])
print("Last item:", colors[-1])

print(colors[1:3])
print(colors[:3])
print(colors[-2:])

# List with different data types
my_list = ["Python", 20, 3.5, True]

print(my_list)

# Conditional Statements
num1 = 15
num2 = 10

if num1 > num2:
    print("num1 is greater than num2")

elif num1 == num2:
    print("Both numbers are equal")

else:
    print("num1 is smaller than num2")


students = ["Ali", "Sara", "Ahmed", "Ayesha"]

if len(students) > 3:
    print("There are more than 3 students")

else:
    print("There are 3 or fewer students")


print("First student:", students[0])