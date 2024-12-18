name = input(" input your name : ")
isStudent = input(" Are you a current student in DLL(Yes/No): ")

if isStudent.lower() == "yes" : 
    yearlevel = input("what year are you currently inrolled in? \nF - Freshmen \nS - Sophomore \nJ - Junior \nR - Senior \nPlease Select which one you are : ")
    if yearlevel.lower() == "f" :
        print(f"Hi, {name}, Freshmen, Welcome to DLL ")
    elif yearlevel.lower() == "s" : 
        print(f"Hi, {name}, Sophomore, Welcome to DLL")
    elif yearlevel.lower() == "j" : 
        print(f"Hi, {name}, Sophomore, Welcome to DLL")
    elif yearlevel.lower() == "r" : 
        print(f"Hi, {name}, Sophomore, Welcome to DLL")
else: 
    print("Thank you for using the program")