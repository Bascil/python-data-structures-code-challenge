# TUPLES
# Tuples are immutable - you cant add/change
# Are suitable for fixed data
# Are faster than lists

# a. Constructor - Create new tuple
x = ()
x = (1, 2, 3) # or just 1, 2, 3 - parentheses are optional
print(x)

x = 2, # the comma tells python its a tuple
print(x)
print(x, type(x))

# Tuples are immutable but member objects may be mutable
x = (1, 2, 3)
# del(x[1]) # fails - 'tuple' object doesn't support item deletion
# x[1] = 8  # fails - 'tuple' object doesn't support item assignment

y = ([1,2], 3)
print(y)
del(y[0][1])
print(y)  # outputs ([1],3)

y += (4,)
print(y) #outputs ([1], 3, 4)




