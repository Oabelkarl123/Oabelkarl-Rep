import os 

isContinue = True 
nt = 0 

while isContinue:
    ask = input(":Do you like to create more triangle (yes/no): ")
    if ask.lower() == "no":
        print("Program Terminated")
        break 
        

    elif ask.lower() == "yes" :
        os.system("cls")
        nt += 1
        for i in range(1, 5):
            for a in range(1, nt + 1):
                for b in range(1, i + 1):
                    print("*", end = " ")
                for c in range(5, i, -1):
                    print(" ", end = " ")
                print(end = " ")
            print()
        continue
    else:
        print("Invalid answer,the only answers are 'yes' or 'no' ")
        continue