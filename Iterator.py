a_set = {1, 2, 3}
b_iterator = iter(a_set)
next(b_iterator)
print(type(a_set))
print(type(b_iterator))


for city in ["Berlin", "Vienna", "Zurich"]:
    print(city)
print("\n")
for city in ("Python", "Perl", "Ruby"):
    print(city)
print("\n")
for char in "Iteration is easy":
    print(char, end=" ")
print("\n")
# list of cities
cities = ["Berlin", "Vienna", "Zurich"]

# initialize the object
iterator_obj = iter(cities)

print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print("\n")

# Function to check object
# is iterable or not
def iterable(obj):
    try:
        iter(obj)
        return True

    except TypeError:
        return False


# Driver Code
for element in [34, [4, 5], (4, 5),
                {"a": 4}, "dfsdf", 4.5]:
    print(element, " is iterable : ", iterable(element))


# String as an iterable
for i in 'chirag':
    print(i)
print('------')
# list as an iterable
for i in [1,2,3]:
    print(str(i*2))



list_1 = [1, 2, 3, 4, 5]
list_2 = iter(list_1)
print(list_2)
# Iterating through iterable(list_1) using for loop.
for element in list_1:
    print(element, end=" ")
print(" ")
# Iterating through iterator(list_2) using for loop.
for element in list_2:
    print(element, end=" ")

print("\n")

list_1 = [1,2,3,4,5]
# Returns an iterator
list_2 = iter(list_1)
print (list_2)
# Calling  iter() function on iterator itself.
list_3 = iter(list_2)
print (list_3)
print (list_2 == list_3)
