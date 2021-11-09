###################################
######## Pass by reference ########
###################################

#  Only for mutable variables
print("\nPass by reference proof (Mutable)")
secret = [1, 101, 456]

def passref(arr):
    arr.pop()
    print(f"Inside Function\t: {arr}")

print(f"Before function\t: {secret}")
passref(secret)
print(f"After function\t: {secret}")

print("\n===========================================")

#  Pass by reference proof (Assigning new value = arg lost its reference)
print("\nPass by reference proof (Assigning new value = arg lost its reference)")
secret = [1, 101, 456]

def passref2(arr):
    arr = [404, 999]
    print(f"Inside Function\t: {arr}")

print(f"Before function\t: {secret}")
passref2(secret)
print(f"After function\t: {secret}")

print("\n===========================================")


###################################
############ Arguments ############
###################################

# Function (with Required, Keyword and Default arguments)
print("\nFunction (with Required, Keyword and Default arguments)")
def myPrint(text, age = 17):
    text = f"myPrint (aged {age}) says: {text}"
    print(text)

myPrint("Wow")
myPrint("Wow", 24)
myPrint("Wow", age = 21)

print("\n===========================================")

# Function Variable-Length (Tuple *)
print("\nFunction Variable-Length (Tuple *)")
def varLenFnTuple(text, *myTuple):
    print(f"Text\t: {text}")
    print(f"myTuple\t: {myTuple}")

    print("Printing each of myTuple:")

    for v in myTuple:
        print(v)
varLenFnTuple("Simple", 12, ["Wow", False], {"wwow":True})

print("\n===========================================")

# Function Variable-Length (Dict **)
print("\nFunction Variable-Length (Dict **)")
def varLenFnTuple(text, **myDict):
    print(f"Text\t: {text}")
    print(f"myTuple\t: {myDict}")

    print("Printing key-value of myDict:")

    for k,v in myDict.items():
        print(f"{k}\t: {v}")

varLenFnTuple("Simple", age=23, single=True, cars=["Bajaj", "Becak", "Perahu Dayung"])

print("\n===========================================")

# Anonymous Function (Lambda)
print("\nAnonymous Function (Lambda)")
product = lambda angka1, angka2: angka1 * angka2

print(f"Product: {product(6, 4)}")

print("\n===========================================")

# Return with docstring
print("\nReturn value")
def splitStringBySpace(text: str):
    '''
    Splits a string by spaces.
    :param text: Input string | str

    :return res: Split string | List[str]
    '''
    res = text.split(' ')
    return res
wow = splitStringBySpace("We are Eternals")
print(wow)

print("\nFunction's docstring:")
print(splitStringBySpace.__doc__)
