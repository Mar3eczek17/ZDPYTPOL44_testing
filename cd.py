import copy
a = [1, 2, [3, 4]]
b = copy.deepcopy(a)
a[2][0] = 10
print(a)
print(b)

x = [4,1]
x.sort()
import bisect
bisect.insort(x, 2)
print(x)

print(bisect.bisect(x,2))