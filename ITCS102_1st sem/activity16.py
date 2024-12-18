for i in range(1, 6):
    for a in range(1, i + 1):
        print(" ", end = " ")
    for o in range(6, i, -1):
        print("*", end = " ")
    print()