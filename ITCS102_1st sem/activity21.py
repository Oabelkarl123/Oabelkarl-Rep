tuloy = True
while tuloy == True:
    name = input("what is your name: ")
count = name
    if name.lower() == "stop":
        print("Loop has now stopped")
        print(f"you have entered {count} number")
        break
        tuloy = False
    else:
        count