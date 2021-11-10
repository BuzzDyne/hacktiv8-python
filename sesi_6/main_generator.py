def counter(low, high=None):
    if high:
        while low <= high:
            yield low
            low += 1
    else:
        while True:
            yield low
            low += 1


for x in counter(1):
    # if x % 20 == 0:
    #     print()
    print(x, end=" ")