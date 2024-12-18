#FARENHEIT TO CELCIUS

print(" FARENHEIT TO CELCIUS CONVERTER PROGRAM")
farenheit = eval(input("Enter the temperature in farenheit:   "))
celcius = ((farenheit - 32 ) * 5)/9  
print (f" {farenheit}, degree farenheit converter to celcius is {round(celcius, 2 )} degree")