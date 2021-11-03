d = {'first':'string value', 'second':[1,2]}
print(d.keys())
print(d.values())
print(d['first'])
print(d.items())

print(d.get('first'))
print(d.pop('first'))
print(d)

print(d.popitem())
print(d)

d1={'a':[1,2]}
print(d1['a'])
d2=d1
d2['a']=[1,2,3,4]
print(d1['a'])
print(d2['a'])
print('-----------------')
d1={'a':[1,2]}
print(d1['a'])
d2=d1.copy()
d2['a']=[1,2,3,4]
print(d1['a'])
print(d2['a'])
print('===================')
d1={'a':[1,2]}
print(d1['a'])
d2=d1
d2['a']=[1,2,3,4]
print(d1['a'])
print(d2['a'])

print(d2)
print(d2.clear())

d = {'a':1, 'b':2, 'c':3}
print(d)
del d['a']
print(d)
d.clear()
print(d)

d2.setdefault('third')
print(d2['third'])

print(d2.fromkeys(['first', 'second']))
print('--------------')
{}.fromkeys(['first','second'])
a = {'first':None, 'second': None}
print(a)

d1 = {'a': 1}
print(d1)
d2 = {'a': 2, 'b': 2}
d1.update(d2)
print(d1['a'])
print(d2['b'])
print((d1))
print((d2))

d = {'first':'string value', 'second':[1,2]}
print([x for x in d.values()])

print([x for x in d.__iter__()])

print([x for x in d.items()])
