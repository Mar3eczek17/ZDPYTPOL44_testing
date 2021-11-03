squares = []
for i in range(1,11):
    squares.append(i**2)

print(squares)

squares_lc = [i**2 for i in range(1, 11)]
print(squares_lc)

odd_numbers = []
for number in range(1,11):
    if number % 2 != 0:
        odd_numbers.append(number)
print(odd_numbers)

odd_numbers_lc = [number for number in range(1, 11) if number % 2 != 0]
print(odd_numbers_lc)

users = [{'name': 'Fred', 'age': 24},
         {'name': 'Cherry', 'age': 27},
         {'name': 'Peter', 'age': 30}]

names = []
for user in users:
    if user['age'] > 25:
        names.append(user['name'])
print(names)


names_ls = [user['name'] for user in users if user['age'] > 25]
print(names_ls)

matrix = []
for row_index in range(0,3):
    row = []
    for col_index in range(0,3):
        if col_index == row_index:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)
print(matrix)

imx = [[1 if c_idx == r_idx else 0 for c_idx in range(0, 3)] for r_idx in range(0, 3)]
print(imx)

squares = {}
for i in range(1, 11):
    squares[i] = i**2
print(squares)

squares = {i: i**2 for i in range(1, 11)}
print(squares)

class Person:

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

persons = { 1: Person(1, "Fred", 26), 2: Person(2, "Ria", 31), 3: Person(3, "Sayid", 23) }

above_25 = {}
for key in persons:
    if persons[key].age > 25:
        above_25[key] = persons[key]
print(above_25)

above_25_dc = {id: person for (id, person) in persons.items() if person.age > 25}
print(above_25_dc)

message = 'Dictionary Comprehensions are able to construct a Dictionary using a single line'
word_count = {}
for word in message.split(" "):
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

word_count_dc = {word: message.split().count(word) for word in set(message.split())}
print(word_count_dc)


class Person:

    def __init__(self, id, name, age, city):
        self.id = id
        self.name = name
        self.age = age
        self.city = city

persons = [ Person(1, "Fred", 26, "San Francisco"), Person(2, "Ria", 31, "San Francisco"), Person(3, "Sayid", 23, "New York City") ]

unique_cities = { person.city for person in persons}
print(unique_cities)