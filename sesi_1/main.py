# Data types
print(type(1))
print(type(1.2))
print(type('1'))
print(type(True))
print()

# Multiple Assignments
a = b = c = "Wow"
print(a, b, c)
print()

# Operator
print(a + b)
print(int(1.7 + 2.3)) # int = floor
print(7 ** 2)
print(8 / 3)
print(8 // 3)
print(7 == 2)
print()

# String
s = 'string'
t = 'manip'

print(s+t)
print(t*2)
print()

# List
a = ['foo', 'bar', 'baz', 'qux']
print(a[0:-1])
print()

# Tuples
t = ('tuple1', 'tuple2', 'tuple3', 'tuple4',)
(a,b, _, _) = t

print(a,b)

# Dictionary
teams = {
    'dictItem0': 0,
    'dictItem1': 1,
    'dictItem2': 2,
    'dictItem3': 3
}
print(teams)

teams['NEWITEM'] = 456
teams['new sub-dict'] = {'name': "Ricky", "age": 22}
print(teams)
print()
