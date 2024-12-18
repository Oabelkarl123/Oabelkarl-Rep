import os
def activity2():
    isconsumer = input("Will you buy a grocery (yes/no) : ")

if isconsumer.lower() == "yes":
	nameitem = input("name of the item : ")
	priceitem = eval(input("price of the item : "))
	age = eval(input("age : "))
	givenamount = eval(input("amount given : "))
	D = round((priceitem * 0.052), 2)
	Dprice = round((priceitem - D), 2)
	tax = round((priceitem * 0.123), 2)
	taxprice = round((priceitem + tax), 2)

if age >= 60 :
	print(f"Hi consumer, you purchased a {nameitem}, with a price of {priceitem}php substract a 5.2% discount ({D}php) to your total purchase. ")
	print(f"Total of : {round((priceitem - D), 2)}")
	print(f"Change :  {round((givenamount - Dprice), 2)}")
	print(f"Thank you for shopping, hope to see you again next time. ")
elif age >= 18 : 
	print(f"Hi consumer, you purchased a {nameitem}, with a price of {priceitem}php plus a 12.3% tax ({tax}php) to your total purchase. ")
	print(f"Total of : {round((priceitem + tax), 2)}")
	print(f"Change :  {round((givenamount - taxprice), 2)}")
	print(f"Thank you for shopping, hope to see you again next time. ")

else: 
	print("Thank you for dropping by. See you again later. ")
 
    
def activity4():
    num1 = eval(input("Enter a number: "))
    num2 = eval(input("Enter anothoer number: "))
    answer = num1 + num2

    print ("The sum of", num1, " + ", num2, " is ", answer)

def activity5():
    print("FARENHEIT TO CELSIUS CONVERTER PROGRAN")
    farenheit = eval(input("Enter the temperature in Farenhiet: "))
    celcius = ((farenheit - 32) * 5)/9
    print (f"{farenheit}, degrees Farenheit converter to celsius is {round(celcius, 2)} degrees")

def activity6():
    x = 5

    print (x)

    x = x + 10

    print (x)

    x = x + 15

    print (x)

    x = x + 20

    print (x)

    X = x + 25

    print (x)

    x = x + 30

    print (x)

isContinue = True
while isContinue:
    ask = input("Select the python file you want to open: \n1.) activity2 \n2.) activity4 \n3.) activity5 \n4.) activity6 \n5.) exit \nInput: ")
    os.system('cls')
    if ask == "1":
        print("Program is running")
        activity2()
    elif ask == "2":
        print("Program is running")
        activity4()
    elif ask == "3":
        print("Program is running")
        activity5()
    elif ask == "4":
        print("Program is running")
        activity6()
    elif ask == "5":
        break
    else:
        continue1