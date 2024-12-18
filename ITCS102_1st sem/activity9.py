user = input("Enter a name:  ")
age = eval(input(" Enter your age: "))

if age >= 1 and age <= 7:
    print(f"Hi {user}, you are a Toddler. ")
elif age >= 8 and age <= 13:
    print(f"Hi {user}, you are a Pre-teen. ")
elif age >= 14 and age <= 18:
    print(f"Hi {user}, you are a Teenager. ")
elif age >= 19 and age <= 31:
    print(f"Hi {user}, you are a tEarly adulthood. ")
elif age >= 32 and age <= 45:
    print(f"Hi {user}, you are a Mid adulthood. ")
elif age >= 46 and age <= 59:
    print(f"Hi {user}, you are a port adulthood. ")
elif age >= 60 and age <= 100:
    print(f"Hi {user}, you are a senior. ")
else: 
    print(f" its impossible you're still alive at that point{user}")