class Team:
   '''
   Contains List of Junior and senior team members
   '''
   def __init__(self):
       self._juniorMembers = list()
       self._seniorMembers = list()
   def addJuniorMembers(self, members):
       self._juniorMembers += members
   def addSeniorMembers(self, members):
       self._seniorMembers += members


# Create team class object
team = Team()
# Add name of junior team members
team.addJuniorMembers(['Sam', 'John', 'Marshal'])
# Add name of senior team members
team.addSeniorMembers(['Riti', 'Rani', 'Aadi'])

# iter(team)
# for member in team:
#    print(member)

def __iter__(self):
    pass


class TeamIterator:
   '''
   Contains List of Junior and senior team members and also overrides the __iter__() function.
   '''
   def __init__(self):
       self._juniorMembers = list()
       self._seniorMembers = list()
   def addJuniorMembers(self, members):
       self._juniorMembers += members
   def addSeniorMembers(self, members):
       self._seniorMembers += members
   def __iter__(self):
       ''' Returns the Iterator object '''
       return TeamIterator(self)


# Get Iterator object from Iterable Team class object
# iterator = iter(team)
# print(iterator)

def __next__(self):
    pass


class TeamIterator:
   ''' Iterator class '''
   def __init__(self, team):
       # Team object reference
       self._team = team
       # member variable to keep track of current index
       self._index = 0
   def __next__(self):
       ''''Returns the next value from team object's lists '''
       if self._index < (len(self._team._juniorMembers) + len(self._team._seniorMembers)) :
           if self._index < len(self._team._juniorMembers): # Check if junior members are fully iterated or not
               result = (self._team._juniorMembers[self._index] , 'junior')
           else:
               result = (self._team._seniorMembers[self._index - len(self._team._juniorMembers)]   , 'senior')
           self._index +=1
           return result
       # End of Iteration
       raise StopIteration

# Create team class object
team = Team()
# Add name of junior team members
team.addJuniorMembers(['Sam', 'John', 'Marshal'])
# Add name of senior team members
team.addSeniorMembers(['Riti', 'Rani', 'Aadi'])
# Get Iterator object from Iterable Team class oject
iterator = iter(team)
# Iterate over the team object using iterator
while True:
    try:
        # Get next element from TeamIterator object using iterator object
        elem = next(iterator)
        # Print the element
        print(elem)
    except StopIteration:
        break

# Iterate over team object(Iterable)
for member in team:
    print(member)