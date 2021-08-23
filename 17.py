# Dictionaries
'''
Are key value pairs
Are associative arrays like Java Hashmap
Dicts are unordered
'''

x = {'pork' : 25.3, 'beef': 33.8, 'chicken': 22.4 }
print(x)

x = dict([('pork', 25.3), ('beef', 33.8), ('chicken', 22.4)])
print(x)

x = dict(pork = 25.3, beef = 33.8, chicken = 22.4)
print(x)

# Add or update
x['shrimp'] = 38.2
print(x)

# Delete an item
del(x['pork'])
print(x)

# Check membership
x = {'pork' : 25.3, 'beef': 33.8, 'chicken': 22.4 }
print('beef' in x)

# Delete all items from dict
x.clear()
print(x)

# delete dict
del(x)

# accessing keys and values

y = {'pork' : 25.3, 'beef': 33.8, 'chicken': 22.4 }
print(y.keys())

y = {'pork' : 25.3, 'beef': 33.8, 'chicken': 22.4 }
print(y.values())

y = {'pork' : 25.3, 'beef': 33.8, 'chicken': 22.4 }
print(y.items())

# check membership in y keys
print('pork' in y)
# or
print('pork' in y.keys())

# check membership in y values
print('claims' in y.values())

# iterating a dict
y = {'pork' : 25.3, 'beef': 33.8, 'chicken': 22.4 }

for key in y:
  print(key , y[key])

# or
for k,v in y.items():
  print(k,v)







