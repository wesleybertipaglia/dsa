# while
i = 1

while i < 6:
    print(i)
    i += 1

# for
for x in range(6):
    print(x)

# for in
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)

# nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# control statements

# break: stop the loop
for x in range(6):
    if x == 3:
        break
    print(x)

# continue: skip the current iteration
for x in range(6):
    if x == 3:
        continue
    print(x)
