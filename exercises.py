import timeit

# l = [1, 2, "a"]
# print(type(l))
# t = (1, 2, "a")
# print(type(t))
# d = {"a":1, "b":2}
# print(type(d))
# c = {1,2,"a"}
# print(type(c))


l = [1,2,3]
print(l[0])
l.append(1)
print(l)

stack = ['a','b']
stack.append('c')
print(stack)

stack.append(['d','e','f'])
print(stack)

stack = ['a', 'b', 'c']
stack.extend(['d', 'e', 'f'])
print(stack)

my_list = ['a','b','c','b', 'a']
print(my_list.index('a'))

my_list = ['a','b','c','b', 'a', 'b']
print(my_list.index('b', 2))

my_list.insert(2, 'a')
print(my_list)

my_list.remove('a')
print(my_list)

print(my_list.pop())
print(my_list)

print(my_list.count('b'))

my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list = ['a', 'c', 'b']
my_list.reverse()
print(my_list)

my_list = [1]
my_list += [2]
print(my_list)

my_list = [1,2]
my_list = my_list*2
print(my_list)

a=[0,1,2,3,4,5]
print(a)
print(a[2:])
print(a[:2])
print(a[2:-1])
print("----------------------")

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a[:])
print(a[::1])
print(a[0::1])
b = [1, 2, 3, 4, 5, 6, 7, 8]
print(b[::-1])

evens = []
for i in range(10):
    if i % 2 ==0:
        evens.append(i)
print(evens)

a = [i for i in range(10) if i % 2 == 0]
print(a)

li = [1, 2, 3]
a = [elem*2 for elem in li if elem>2]
print(a)

stack = ['a', 'b', 'c', 'd']
stack.append('e')
stack.append('f')
print(stack)
print(stack.pop())
print(stack)

queue = ['a', 'b', 'c', 'd']
queue.append('e')
queue.append('f')
print(queue)
print(queue.pop(0))


l2 = list(l)
l2 = l[:]
import copy
l2 = copy.copy(l)

a = [1,2,[3,4]]
# b = a[:]
a[2][0] = 10
print(a)
print(b)

import copy
b = copy.deepcopy(a)
print(a)
print(b)