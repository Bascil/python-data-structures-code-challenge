# Slicing - Slice out substrings, sublists, subtuples using indexes
# [start: end+1: step] 
# start is inclusive, end is non inclusive
# This is the same for lists and tuples

x = 'computer'
print(x[1:4])

print(x[1:6:2])

print(x[3:]) # Everything from the third item

print(x[:5]) # Begining upto the sixth item

print(x[-1]) # Last item in the string - negative index

print(x[-3:]) # Last three items

print(x[:-2]) # Everything except the last 2 elements



