
name = "Ricky"
age = 95

# if
print("\n=========== Inside If ===========")
if age >= 21:
    print("Anda sudah dewasa")
elif age >= 100:
    print("Anda ngibul")
else:
    print("Pulang nak.")

# Shorthand If
print("\n=========== Inside Shorthand If ===========")
print("Halo pak") if name == "Ricky" else print("Siapa kamu")

# While
print("\n=========== Inside While ===========")
while age < 100:
    age += 1
    print(f"Selamat ulang tahun ke-{age}") 

# break and continue
print("\n=========== Inside continue ===========")
age = 95
while age < 100:
    age += 1

    if age == 98:
        continue
    print(f"Selamat ulang tahun ke-{age}") 

print("\n=========== Inside break ===========")
age = 95
while age < 100:
    age += 1

    if age == 98:
        break
    print(f"Selamat ulang tahun ke-{age}") 

print("\n=========== Inside While-Else ===========")
age = 98
while age < 100:
    age += 1
    print(f"Curr age {age}")
else:
    print(f"We are inside else, age:{age}")
    

print("\n=========== Inside Shorthand While ===========")
money = 0
while money < 5: money += 1; print(f"Your money {money}")

print("\n=========== Inside For ===========")
items = ['a', 'b', 'c', 'd', 'e']
for i in items:
    print(i, end=", ")

print("\n=========== Inside Range ===========")
for i in range(5):
    print(i, end="")
