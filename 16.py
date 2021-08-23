# SETS
'''
- Sets store non duplicate/unique items
- Have very fast access compared to lists
- Sets are unordered
- Suitable for math set operations such as unions and intersections
'''

x = {3, 5, 3, 5}
print(x)  # {3,5}

x = [2, 3, 4]
z = set(x)
print(z) # {2,3,4}

# a. add - add an iten to a set
x = {3, 5, 8}
x.add(7)
print(x)  # {8,3,5,8,7} unordered

# b. remove -remove an item from a set
x = {3, 5, 8}
x.remove(3)
print(x) # {8,5}

# c. Length - get the length of a set
x = {3, 5, 8, 7}
print(len(x))

# d. membership 
x = {3, 5, 8, 7}
print(5 in x)

# e. pop - pop a random item from set x
x = {3, 5, 8, 7}
print(x.pop(), x)

# f.clear - delete all items from a set
x.clear()
print(x)

'''
Mathematical Set Functions
Intersection(AND)
Union(OR |)
Symmetric Difference(XOR)
Subset
Superset
'''

# Intersection - AND - Set 1 & Set 2
s1 = { 1, 2, 3}
s2 = { 3, 4, 5}
print(s1 & s2) # appears in both s1 and s2

# Union - OR - Set 1 OR Set 2
s1 = { 1, 2, 3}
s2 = { 3, 4, 5}
print(s1 | s2)

# Symmetric difference - XOR - s1 ^ s2
# includes items in set 1 but not in set 2 or item in set 2 but not in set 1
s1 = { 1, 2, 3}
s2 = { 3, 4, 5}
print(s1 ^ s2)


