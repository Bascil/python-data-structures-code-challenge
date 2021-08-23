# Python Built in Data Structures: Strings, List, Tuples, Dictionaries

# LISTS
# Is a general purpose data structure and is the most widely used
# You can grow and shrink size as needed
# It is sortable hence useful for sorting data

# a. Constructor - Create a new list
# Create an empty list
x = list()
print(x)

# You can pass the items you want in the list in square brackets
y = ['a', 25, 'dog', 8.4]
print(y)

# b. List Comprehension
a = [x for x in range(8)]
print(a)

# c. Delete - delete a list or an item in the list
x = [5, 3, 8, 6]
del(x[1])
print(x)

del(x) # x no longer exists
# print(x) throws an error because x is not defined

# d. append - append/add an item to a list
x = [5, 3, 8, 6]
x.append(7)
print(x)

# e. extend - append a sequence to a list, similar to +, combining
# two separate list to one
x = [5, 3, 8, 6]
y = [12, 13]
x.extend(y)
print(x)

# f. insert - insert an item at a given index e.g insert a 7 at the 1st position
x = [5, 3, 8, 6]
x.insert(1,7)
print(x)

x.insert(1, ['a','m'])
print(x)

# g. pop - pops/removes the last item off the list and returns item
x = [5, 3, 8, 6]
x.pop()
print(x)

# h. remove - remove the first instance of an item
x = [5, 3, 8, 6, 3]
x.remove(3)
print(x)

# i.reverse - reverse the order of a list, it changes the original list
x = [5, 3, 8, 6]
x.reverse()
print(x)

# j. sort - puts the items in sorted order
x = [5, 3, 8, 6]
x.sort()
print(x)

# k. reverse sort - sorts the items in descending order, 
# use reverse=True parameter to the sort function
x = [5, 3, 8, 6]
x.sort(reverse=True)
print(x)



