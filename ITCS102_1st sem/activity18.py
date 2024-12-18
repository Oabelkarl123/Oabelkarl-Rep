triangle = eval(input("Enter number of triangle you want:  "))

for i in range(1, 6):
    for a in range(1, triangle, 1):
        for b in range(1, i + 1):
            print("*", end= " ")
        for c in range(5, i, -1):
            print(" ", end= " ")
        print(end=" ")
    print()
                      
