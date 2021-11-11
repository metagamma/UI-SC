import sys
import math
import random
import threading
import time
from functools import reduce

print("Hello World")

# Accept user input and store it in a variable
# name = input("What is your name ")
# print("Hi ", name)

# If you want to extend a statement to multiple
# lines you can use parentheses or \

# If you want to extend a statement to multiple
# lines you can use parentheses or \
mixed_var = (
    1 + 2 + 3
)

v1 = 1 + 2 \
    + 3

# Put multiple statements on 1 line
v1 = 5
v1 = v1 - 1

# Inline comment

''' 
Multiline 
comment 
'''

b1 = b2 = 20

a = 1
a = "a"  # Datatypes can change

# ----- VARIABLES -----
# Variables are names assigned to values
# The 1st character must be _ or a letter
# Then you can use letters, numbers or _
# Variable names are type sensitive

# integer, floats, complex numbers, strings, booleans
v2 = 1
V2 = 2  # v1 is different from V1

# How to get the type
print(type(100))

# There is no limit to the size of integers
# This is a way to get a practical max size
print(sys.maxsize)

# Floats are values with decimal values
# This is how to get a max float
print(sys.float_info.max)

# floats are accurate until 15 digits
f1 = 1.1111111111111111
f2 = 1.1111111111111111
f3 = f1 + f2
print("Accuracy: ", f3)

# complex numbers have real part + imaginary part ex...
cmplx = 5 + 6j

# Booleans are either True or False
bl = False

# Strings are surrounded by ' or "
str1 = "Escape Sequence \' \" \t \\ \n"

str2 = '''Triple quoted string ' " '''

# You can cast to different types with int, float,
# str, chr
print("Cast 1", type(int(5.4)))
print("Cast 2", type(str(5.4)))
print("Cast 3", type(chr(97)))
print("Cast 4", type(ord('a')))

# ----- OUTPUT -----
# You can define a separator for print
print(12, 21, 1974, sep="/")

# Eliminate newline
print("no new line", end='')

# String formating
print("\n%04d %s %.2f %c" % (1, "derek", 1.21321, 'A'))

# Basic math functions
print("5 + 2", 5 + 2)
print("5 - 2", 5 - 2)
print("5 * 2", 5 * 2)
print("5 / 2", 5 / 2)
print("5 % 2", 5 % 2)
print("5 ** 2", 5 ** 2)
print("5 // 2", 5 // 2)  # int division

# Shortcuts
i1 = 2
i1 += 1
print("i1", i1)

# Math Functions
print("abs(-1) ", abs(-1))
print("max(5, 4) ", max(5, 4))
print("min(5, 4) ", min(5, 4))
print("pow(2, 2) ", pow(2, 2))
print("ceil(4.5) ", math.ceil(4.5))
print("floor(4.5) ", math.floor(4.5))
print("round(4.5) ", round(4.5))
print("exp(1) ", math.exp(1))  # e**x
print("log(e) ", math.log(math.exp(1)))
print("log(100) ", math.log(100, 10))  # Base 10 Log
print("sqrt(100) ", math.sqrt(100))
print("sin(0) ", math.sin(0))
print("cos(0) ", math.cos(0))
print("tan(0) ", math.tan(0))
print("asin(0) ", math.asin(0))
print("acos(0) ", math.acos(0))
print("atan(0) ", math.atan(0))
print("sinh(0) ", math.sinh(0))
print("cosh(0) ", math.cosh(0))
print("tanh(0) ", math.tanh(0))
print("asinh(0) ", math.asinh(0))
print("acosh(pi) ", math.acosh(math.pi))
print("atanh(0) ", math.atanh(0))
print("hypot(0) ", math.hypot(10, 10))  # sqrt(x*x + y*y)
print("radians(0) ", math.radians(0))
print("degrees(pi) ", math.degrees(math.pi))

# Generate random number
print("Random", random.randint(1, 100))

# This prints True
print(math.inf > 0)

# This prints NaN (not a real number)
print(math.inf - math.inf)

# ----- CONDITIONALS -----
# Comparison Operators : < > <= >= == !=
# if, else & elif execute different code depending
# on conditions

age = 30
# Python uses indentation to define all the
# code that executes if the above is true
if age > 21:
    print("You can drive a tractor trailer")
elif age >= 16:
    print("You can't drive a car")
else:
    print("You can't drive")

# Make more complex conditionals with logical operators
# Logical Operators : and or not

if age < 5:
    print("Stay Home")
elif (age >= 5) and (age <= 6):
    print("Go to kindergarden")
elif (age > 6) and (age <= 17):
    print("Grade", (age - 5))
else:
    print("College")

# Ternary operator in Python
# condition_true if condition else condition_false
canVote = True if age >= 10 else False
print(canVote)

# ----- STRINGS -----
# Raw strings ignore escape sequences
print(r"I'll be ignored \t\t Hello...")

# Combine strings with +
print("Hello" + "youuu")

# Get string length
str3 = "Hello to myself"
print("Length", len(str3))

# Character at index
print("1st", str3[0])

# Last character
print("Last", str3[-1])

# 1st 3 chrs
print("1st to 3rd", str3[0:3])

# Get every other character
print("Every other,", str3[0:-1:2])  # from first to the end every 2 elements

# You can't change an index value like this
# str3[0] = "a" because strings are immutable
# (Can't Change)
# You could do this
str3 = str3.replace("Hello", "Goodbye")
print(str3)

# You could also slice front and back and replace
# what you want to change
str3 = str3[:8] + "y" + str3[9:]
print(str3)

# Test if string in string
print("you" in str3)

# Test if not in
print("you" not in str3)

# Find first index for match or -1
print("You index", str3.find("yo"))

# Trim white space from right and left
# also there are lstrip() and rstrip(s)
print("            whitespace trimmed".strip())

# Convert a list into a string and separate with a line
print(" - ".join(["Some", "Words", "BLBABABABA"]))

# Convert string into a list with a defined separator
# or delimiter
print("A string babblalal".split(" "))

# Formatted output with f-string
int1 = int2 = 5
print(f'{int1} + {int2} = {int1 + int2}')

# Is letter or number
print("LowEr CASE StrinG".lower())
print("LowEr CASE StrinG".upper())

# Is letter or number
print("Astring123".isalnum())

# Is characters
print("Astring".isalpha())

# Is numbers
print("123".isdigit())

# ----- LISTS -----
# Lists can contain mutable pieces of data of
# varying data types or even functions
l1 = [1, 314, "Dante", True]
print(l1)

# Get length
print("Length", len(l1))

# Get value at index
print("1st", l1[0])
print("Last", l1[-1])

# Change value
l1[0] = 2
print(l1)

# Change multiple values
l1[2:4] = ["Bob", False]  # from index 2 up to 4 but not including 4
print(l1)

# Insert at index without deleting
# Also l1.insert(2, "Paul")
l1[2:2] = ["Paul", 9]

# Add to end (Also l1.extend([5, 6]))
l2 = l1 + ["Egg", 4]
print("l2", l2)

# Remove a value
l2.remove("Paul")
print("l2", l2)

# Remove at index
l2.pop(0)
print("l2", l2)

# Add to beginning (Also l1.append([5, 6]))
l2 = ["Egg", 4] + l1
print("l2", l2)

# Multidimensional list
l3 = [[1, 2], [3, 4]]
print("[1,1]", l3[1][1])

# Does value exist
print("1 exists", (1 in l1))

# Min & Max
print("Min", min([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print("Max", max([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Slice out parts
print("1st 2", l1[0:2])
print("Every other", l1[0:-1:2])
print("Reverse", l1[::-1])

# ----- LOOPS -----
# While : Execute while condition is True

w1 = 1
while w1 < 5:
    print(w1)
    w1 += 1

w2 = 0
while w2 <= 20:
    if w2 % 2 == 0:
        print(w2)
    elif w2 == 9:
        # Forces the loop to end all together
        break
    else:
        # Shorthand for i = i + 1
        w2 += 1
        # Skips to the next iteration of the loop
        continue
    w2 += 1

# Cycle through list
l4 = [1, 3.14, "Derek"]
while len(l4):
    print(l4.pop(0))

# For Loop
# Allows you to perform an action a set number of times
# Range performs the action 10 times 0 - 9
# end="" eliminates newline
for x in range(0, 10):
    print(x, ' ', end="")
print('\n')

# Cycle through list
for x in l4:
    print(x)

# You can also define a list of numbers to
# cycle through
for x in [2, 4, 6]:
    print(x)

# You can double up for loops to cycle through lists
num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
for i in range(len(num_list)):
    for j in range(len(num_list[i])):
        print(num_list[i][j], ' ', end="")
print('\n')

# ----- ITERATORS -----
# You can pass an object to iter() which returns
# an iterator which allows you to cycle
l5 = [6, 9, 12]
itr = iter(l5)
print(next(itr))
print(next(itr))

# ----- RANGES -----
# The range() function creates integer iterables
print(list(range(0, 5)))

# You can define step
print(list(range(0, 10, 2)))
print("\n")

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])

# ----- TUPLES -----
# Tuples are just like lists except they are
# immutable
t1 = (1, 3.14, "Derek")

# Get length
print("Length", len(t1))

# Get value / values
print("1st", t1[0])
print("Last", t1[-1])
print("1st 2", t1[0:2])
print("Every other", t1[0:-1:2])
print("Reverse", t1[::-1])

# Everything you can do with lists you can do with
# tuples as long as you don't change values

# ----- DICTIONARIES -----
# Dictionaries are lists of key / value pairs
# Keys and values can use any data type
# Duplicate keys aren't allowed
heroes = {
    "Superman": "Clark Kent",
    "Batman": "Bruce Wayne"
}

# This is other way of defininf a dictionary
villains = dict([
    ("Lex Luthor", "Lex Luthor"),
    ("Loki", "Loki")
])

print("Legth", len(heroes))

# Get value by key
# Also heroes.get("Superman")
print(heroes["Superman"])

# Add more
heroes["Flash"] = "Barry Allan"

# Change a value
heroes["Flash"] = "Barry Allen"

# Get list of tuples
print(list(heroes.items()))

# Get list of keys and values
print(list(heroes.keys()))
print(list(heroes.values()))

# Delete
del heroes["Flash"]

# Remove a key and return it
print(heroes.pop("Batman"))

# Search for key
print("Superman" in heroes)

# Cycle through a dictionary
for k in heroes:
    print(k)

for v in heroes.values():
    print(v)

# Formatted print with dictionary mapping
d1 = {"name": "bread", "price": .88}
print("%(name)s costs $%(price).2f" % d1)

# ----- SETS -----
# Sets are lists that are unordered, unique
# and while values can change those values
# must be immutable
s1 = set(["Derek", 1, 564654])

# Other way of declaring a set
s2 = {"Paul", 1}

# Size
print("Length", len(s2))

# Join sets
s3 = s1 | s2
print(s3)

# Add value
s3.add("Doug")
# Remove value
s3.discard("Derek")

# Remove random value
print("Random", s3.pop())

# Add values in s2 to s3
s3 |= s2

# Return common values (You can include multiple
# sets as attributes)
print(s1.intersection(s2))

# All unique values
print(s1.symmetric_difference(s2))

# Values in s1 but not in s2
print(s1.difference(s2))

s3.clear()

# Frozen sets can't be edited
s4 = frozenset(["Paul", 7])

# ----- FUNCTIONS -----
# Functions provide code reuse, organization
# and much more
# Add 2 values using 1 as default
# You can define the data type using function
# annotations


def get_sum(num1: int = 1, num2: int = 1):
    return num1 + num2


print(get_sum(5, 4))

''' 
Simple way:

def get_sum(num1, num2):
    return num1 + num2

'''

# Accept multiple values


def get_sum2(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


print(get_sum2(1, 2, 3, 4, 5, 6))

# Return multiple values


def next_2(num):
    return num + 1, num + 2


i1, i2 = next_2(5)
print(i1, i2)

# A function that makes a function that
# multiplies by the given value


def mult_by(num):
    # You can create anonymous (unnamed functions)
    # with lambda
    return lambda x: x * num


print("3 * 5 =", (mult_by(3)(5)))

# Pass a function to a function


def mult_list(list, func):
    for x in list:
        print(func(x))


mult_by_4 = mult_by(4)
mult_list(list(range(0, 5)), mult_by_4)

# Create list of functions
power_list = [lambda x: x ** 2,
              lambda x: x ** 3,
              lambda x: x ** 4]

# ----- MAP -----
# Map is used to execute a function on a list
one_to_for = range(1, 5)
def times2(x): return x * 2


print(list(map(times2, one_to_for)))

# ----- FILTER -----
# Filter selects items based on a function
# Print out the even values from a list
print(list(filter((lambda X: X % 2 == 0), range(1, 11))))

# ----- REDUCE -----
# Reduce receives a list and returns a single
# result
# Add up the values in a list
print(reduce(lambda x, y: x + y, range(1, 6)))

# ----- EXCEPTION HANDLING -----
# You can handle errors that would otherwise
# crash your program
# By giving the while a value of True it will
# cycle until a break is reached
while True:
    # If we expect an error can occur surround
    # potential error with try
    try:
        number = int(input("Please enter a number: "))
        break
    # The code in the except block provides
    # an error message to set things right
    # We can either target a specific error
    # like ValueError
    except ValueError:
        print("You didn't enter a number")
    # We can target all other errors with a
    # default
    except:
        print("An unknown error occured")

print("Thank you")

# ----- FILE IO -----
# We can save and read data from files
# We start the code with with which guarantees
# the file will be closed if the program crashes
# mode w overwrites file
# mode a appends
with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
    # You can write to the file with write
    # It doesn't add a newline
    my_file.write("Some random text \nMore random text\nand more")

# Open a file for reading
with open("mydata.txt", encoding="utf-8") as my_file:
    print(my_file.read())

# Find out if the file is closed
print(my_file.closed)

# ---------- RECURSIVE FUNCTIONS ----------
# A function that refers to itself is a recursive function

# Calculating factorials is commonly done with a recursive
# function 3! = 3 * 2 * 1


def factorial(num):
    # Every recursive function must contain a condition
    # when it ceases to call itself
    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result

# 1st : result = 4 * factorial(3) = 4 * 6 = 24
# 2nd : result = 3 * factorial(2) = 3 * 2 = 6
# 3rd : result = 2 * factorial(1) = 2 * 1 = 2
