# Creating lists with List Complrehension

'''
new_list = [transform sequence [filter]]
'''
# Get values within a range
under_10 = [x for x in range(10)]
print('under 10: ' + str(under_10))

# Get Squared values
squares = [x**2 for x in under_10]
print('squares: ' + str(squares))

# Get odd numbers
odds = [x for x in range(10) if x % 2 == 1]
print('odds: ' + str(odds))

# Get multiples of x
ten_x = [x * 10 for x in range(10)]
print('ten_x: ' + str(ten_x))

# Get all numbers from a string
s = 'I l0ve 2 go t0 the store 7 times a week'
nums = [x for x in s if x.isnumeric()]
print('nums: ' + ''.join(nums))

# Get the index of a list item
names = ['basil', 'otieno', 'ndonga']
idx = [k for k, v in enumerate(names) if v == 'otieno']
print('index: ' + str(idx[0]))

