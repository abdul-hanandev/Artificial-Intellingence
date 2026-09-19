# Lab 2
# Iterative Structures in Python

# While Loop
count = 0

while count < 3:
    count = count + 1
    print("Hello", count)


# For Loop
names = ["Ali", "Hanan", "Ahmed"]

for name in names:
    print(name)


# Iterating through a List
languages = ["Python", "C++", "Java"]

for language in languages:
    print(language)


# Iterating through a Tuple
subjects = ("AI", "Database", "HCI")

for subject in subjects:
    print(subject)


# Iterating through a String
word = "Python"

for letter in word:
    print(letter)


# Iterating using Index
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(i, fruits[i])


# Continue Statement
for letter in "geeksforgeeks":

    if letter == "e" or letter == "s":
        continue

    print(letter)


# Break Statement
for letter in "geeksforgeeks":

    if letter == "e" or letter == "s":
        break

    print(letter)


# Function
def my_function():
    print("Hello from a function")


my_function()


# Function with Parameter
def greet(name):
    print("Welcome", name)


greet("Abdul Hanan")
greet("Ali")


# Default Parameter
def country(country="Pakistan"):
    print("I am from", country)


country("Turkey")
country()


# Passing List as Parameter
def show_fruits(food):

    for fruit in food:
        print(fruit)


fruits = ["apple", "banana", "cherry", "orange"]

show_fruits(fruits)


# Return Value
def multiply(x):
    return 5 * x


print(multiply(3))
print(multiply(5))
print(multiply(9))


# Keyword Arguments
def child(child3, child2, child1):
    print("The youngest child is", child3)


child(
    child1="Emil",
    child2="Tobias",
    child3="Linus"
)


# Class and Object
class MyClass:
    x = 5


obj = MyClass()

print(obj.x)


# Constructor and Object Method
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)
        print("My age is", self.age)


person1 = Person("Hanan", 22)

print(person1.name)
print(person1.age)

person1.introduce()