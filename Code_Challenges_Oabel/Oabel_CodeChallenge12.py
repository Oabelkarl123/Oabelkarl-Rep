for x in range(6, 0, -1):
    for y in range(1, x):
        print(" ", end= " ")
    for z in range(6, x , -1):
        print("*", end=" ")
    for w in range(6, x, -1):
        print("*", end=" ")
    print()

for i in range(4):
    print("        * *")
