def mygenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30

gen = mygenerator()
next(gen)
next(gen)
next(gen)

def mygenerator():
    print('First item')
    yield 10

    return

    print('Second item')
    yield 20

    print('Last item')
    yield 30

gen = mygenerator()
next(gen)
# next(gen)

def get_sequence_upto(x):
    for i in range(x):
        yield i


seq = get_sequence_upto(5)
next(seq)
next(seq)
next(seq)
next(seq)
next(seq)
# next(seq)

def square_of_sequence(x):
    for i in range(x):
        yield i*i

gen = square_of_sequence(5)
while True:
    try:
        print ("Received on next(): ", next(gen))
    except StopIteration:
        break

squres = square_of_sequence(5)
for sqr in squres:
    print(sqr)

# Python3 code to demonstrate
# yield keyword

# generator to print even numbers
def print_even(test_list):
    for i in test_list:
        if i % 2 ==0:
            yield i

# initializing list
test_list = [1,4,5,6,7]

# printing initial list
print("The original list is: " + str(test_list))

# printing even numbers
print("The even numbers in list are: ", end=" ")
for j in print_even(test_list):
    print(j, end=" ")

# A Python program to generate squares from 1
# to 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1
def nextSquate():
    i=1

    # An Infinite loop to generate squares
    while True:
        yield i*i
        i += 1  # Next execution resumes
                # from this point

# Driver code
for num in nextSquate():
    if num > 100:
        break
    print(num)

# Python3 code to demonstrate yield keyword

# Checking number of occurrence of
# geeks in string

# generator to print even numbers
def print_even(test_string):
    for i in test_string:
        if i == "geeks":
            yield i

# initializing string
test_string = " The are many geeks around you, \
              geeks are known for teaching other geeks"

# printing even numbers using yield
count = 0
print("The number of geeks in string is : ", end=" ")
test_string = test_string.split()

for j in print_even(test_string):
    count = count + 1
print(count)


squres = (x*x for x in range(5))
print(next(squres))
print(next(squres))
print(next(squres))
print(next(squres))
print(next(squres))

print(sum(x*x for x in range(5)))

print('----------------')

# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# It returns an object but does not start execution immediately.
a = my_gen()
# We can iterate through the items using next().
next(a)
# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and theirs states are remembered between successive calls.
next(a)
next(a)
# Finally, when the function terminates, StopIteration is raised automatically on further calls.
# next(a)

# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)