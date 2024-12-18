input = eval(input("Enter the amount of triangle(s) you want to print:  "))
             
for i in range(1, 5):
    for a in range(1, input + 1):
        for b in range(1, i + 1):
            print("*", end=" ")
        for c in range(5, i, -1):
            print(" ", end=" ")
        print(end=" ")
    print()