def counter(low, high=None):
    if high:
        while low <= high:
            yield low
            low += 1
    else:
        while True:
            yield low
            low += 1

print(type(counter(1)))

for x in counter(1,3):
    # if x % 20 == 0:
    #     print()
    print(x, end=" ")

x = counter(1,3)

print(next(x))
print(next(x))
print(next(x))
