

# File open
try:
    f = open('data/test.txt', 'w')
finally:
    f.close()

# Write to File
with open('data/cobTulis.txt', 'w', encoding= "utf-8") as f:
    f.write("Apa Apaabn saya?\n")
    f.write("Apa nama kamu?\n")
    f.write("Apa nama kita?\n")

# Read File
with open('data/cobTulis.txt', 'r', encoding="utf-8") as f:
    print(f"Reading first 5 data: {f.read(2)}")
    print(f"Reading the rest of data:\n{f.read()}")

    print(f"Tell\t\t\t: {f.tell()}")
    f.seek(0)
    print(f"Tell after f.seek(0)\t: {f.tell()}")

    print(f"\nReading all the data:\n{f.read()}")

    f.seek(0)

    print(f"Reading line per line:")
    for i, line in enumerate(f):
        print(f"Line {i}: {line}")

    f.seek(0)

    print("Print single line (and all lines in an array):")
    print(f.readline())
    print(f.readlines())
