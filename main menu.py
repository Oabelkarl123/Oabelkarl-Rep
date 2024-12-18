name = input("Hi, what is your name: ")
print(f"Hi, {name}")
start = input("Do you want to start a program? yes or no: ")

# Change the "No" to "no" for correct comparison
if start.lower() == "no":  # "no" is now lowercase
    print("Thank you for using the program")
elif start.lower() == "yes":  # "yes" in lowercase will match regardless of case
    print("**************************************\n                -Main Menu-")

    print("       1. PRINTING IN PYTHON")
    print("       2. VARIABLES")
    print("       3. OPERATORS")
    print("       4. CONDITIONALS")
    print("       5. LOOPS")
    print("       6. LIST")
    print("       7. FUNCTIONS")
    print("       8. EXIT")
    
num = input("Enter the number you want in the main menu: ")

    # Handling Menu Option 1
if num == "1":
        print("\n     The print() function prints the specified message to the screen, or other standard output device. \nThe message can be a string, or any other object, the object will be converted into a string before written to the screen.")
    
        print("**************************************************************************\n                -Menu in Printing Python-")

        print("       1. Print with the ‘print’ function")
        print("       2. Print with string formatting")
        print("       3. Print with the ‘str.format()’ method")
        print("       4. Print with the ‘f-string’ syntax")
        print("       5. Print to a file or a stream")

        num2 = input("Enter the number you want in the menu of printing no.1: ")

        if num2 == "1":
            
            print("The most basic way to print in Python is to use the ‘print’ function. This function takes one or more arguments, which can be variables, strings, or any other data type. The ‘print’ function automatically adds a new line character at the end of the output, so each subsequent print statement starts on a new line.")
            print("Example 1:")
            print("print('hello, world!')")
            print("Output: hello, world!")

        elif num2 == "2":
            print("String formatting is a powerful technique that allows you to insert values into a string. In Python, you can use the ‘%’ operator to format a string. This operator takes a string on the left side and one or more values on the right side, separated by commas.")
            print("Example 1: Printing a formatted string")
            print("name = 'Alice'")
            print("age = 25")
            print('%s is %d years old." % (name, age)')  # Corrected string formatting
            print("Output: Alice is 25 years old.")

        elif num2 == "3":
            print("The ‘str.format()’ method is a newer, more versatile way of formatting strings in Python. This method allows you to insert values into a string using curly braces ‘{}’, and then pass those values as arguments to the ‘format()’ method.")
            print("Example 1: Printing a formatted string using 'str.format()'")
            print("name = 'Bob'")
            print("age = 30")
            print('{} is {} years old.".format(name, age)')
            print('Output: Bob is 30 years old.')
        
        elif num2 == "4":
            print("The ‘f-string’ syntax is a newer, even more concise way of formatting strings in Python. This syntax allows you to embed expressions directly into string literals, by prefixing the string with the letter ‘f’.")
            print("Example 1: Printing an f-string")
            print("name = 'carol'")
            print("age = 35")
            print('print(f"#{name} is #{age} years old")')  # just remove the hashtag if you want to use it 
            print("output: carol is 35 years old")

        elif num2 == "5":
            print("In addition to printing to the console, you can also print to a file or a stream in Python. This can be useful when you want to save the output for later analysis or to share with others. To do this, you can use the ‘print’ function with the ‘file’ keyword argument.")
            print("Example 1: Printing to a file")
            print("with open('output.txt', 'w') as f:")
            print("    print('This line will be written to a file.', file=f)")

    # Handling Menu Option 2
if num == "2":
        print("Python has no command for declaring a variable.")
        print("A variable is created the moment you first assign a value to it.")
        print("Here is an example:")
        print("x = 5")
        print("y = 'John'")
        print("print(x)")
        print("print(y)")
        print("\nVariables do not need to be declared with any particular type, and can even change type after they have been set.")
        print("x = 4")
        print("x = 'Sally'")
        print("print(x)")
        print(" ******************************************** \n             -CASTING- ")
        print("If you want to specify the data type of a variable, this can be done with casting")
        print("x = str(3)    # x will be '3'")
        print("y = int(3)    # y will be 3")
        print("z = float(3)  # z will be 3.0")
        
if num == "3":
        print("*******************************************************************\n                    ARITHMETIC OPERATORS")


        print('+ , - Addition / Concatination(String Combination)')
        print("- - Subtraction")
        print(' *() - Multiplication ')
        print("/ - Division ")
        print("% - Modulus")
        print("** - Exponentiation ")
        print("// - Floor Division ")

        print("VARIABLES -- placeholder of Information / Data.")

        print("x  +  y = 15")

        print("Byproduct of Programming is a Software Application , Software application capable of processing information.")

        print("DATA TYPES  - Describes what type of information is being processed.")

        print('Primitive Data types ( Beginner Data types)')

        print("Integer Data Type - Otherwise known as INT, Integer data types are numeric data types, more specially whole number Data Types.")
        print("e.g Age, No. of Students, LRN Number") 

        print("Float Data Type - Numeric Data expressed with Decimal Points. (e.g Prices, Grades, Temperatures ) , Precision values.")

        print("Strings - These are alpha numeric Values ( e.g. Name, Address, email, birthday Month, school, section ) , string values are expressed using")
        print("a pair double quotation ("") or a pair of single quotation (' ')")

        print("Boolean - Data Types expressed in either TRUE OR FALSE.")

        print("VARIABLE NAMING CONVENTIONS / PROTOCOL / PRACTICE ")

        print("variable names cannot start with a number ")
        print("variables name cannot have spaces ")
        print("variables names should avoid using special characters / symbol ")
    
if num == "4":
        print("*******************************************************************\n                    PYTHON CONDITIONS AND IF STATEMENTS")
        print("Python supports the usual logical conditions from mathematics:")
        print("Equals: a == b")
        print("Not Equals: a != b")
        print("Less than: a < b")
        print("Less than or equal to: a <= b")
        print("Greater than: a > b")
        print("Greater than or equal to: a >= b")
        

        print("These conditions can be used in several ways, most commonly in 'if statements' and loops.")

        print("An 'if statement' is written by using the if keyword.")

        print("***************************************************************** \n                     IDENTATION ")      

        print("Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.")                 
        
        print("Example")
        print("If statement, without indentation (will raise an error):")

        print("a = 33")
        print("b = 200")
        print("if b > a:")
        print("print('b is greater than a') # you will get an error")


        print("***************************************************************** \n                     -ELIF- ")


        print("The elif keyword is Python's way of saying 'if the previous conditions were not true, then try this condition'.")
        print("a = 33")
        print("b = 33")
        print("if b > a:")
        print("  print('b is greater than a')")
        print("elif a == b:")
        print("  print('a and b are equal')")
        
        print("***************************************************************** \n                     -ELSE- ")


        print("The else keyword catches anything which isn't caught by the preceding conditions.")
        print("Example")
        print("a = 200")
        print("b = 33")
        print("if b > a:")
        print("  print('b is greater than a')")
        print("elif a == b:")
        print("  print('a and b are equal')")
        print("else:")
        print("print('a is greater than b'')")

        print("***************************************************************** \n                     -SHORT HAND IF- ")

        print("If you have only one statement to execute, you can put it on the same line as the if statement.")
        print("Example")
        print("One line if statement:")
        print("if a > b: print('a is greater than b')")

        print("***************************************************************** \n                     -SHORT HAND IF...ELSE- ")

        print("If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:")
        print("Example")
        print("One line if else statement:")
        print("a = 2")
        print("b = 330")
        print('print("A") if a > b else print("B")')

        print("***************************************************************** \n                     -AND- ")
        print("The and keyword is a logical operator, and is used to combine conditional statements:")

        print("Example")
        print("Test if a is greater than b, AND if c is greater than a:")

        print("a = 200")
        print("b = 33")
        print("c = 500")
        print("if a > b and c > a:")
        print("Both conditions are True")

        print("***************************************************************** \n                     -OR- ")

        print("The or keyword is a logical operator, and is used to combine conditional statements:")
        print("Example")
        print("Test if a is greater than b, OR if a is greater than c:")
        print("a = 200")
        print("b = 33")
        print("c = 500")
        print("if a > b or a > c:")
        print(' print("At least one of the conditions is True")')

        print("***************************************************************** \n                     -NOT- ")
        
        print(" The not keyword is a logical operator, and is used to reverse the result of the conditional statement:")


        print("EXAMPLE")

        print("Test if a is NOT greater than b:")

        print("a = 33")
        print("b = 200")
        print("if not a > b:")
        print("  print('a is NOT greater than b'')")

        print("***************************************************************** \n                     -NESTED IF- ")
        
        print("You can have if statements inside if statements, this is called nested if statements.")

        print("Example")
        
        print("x = 41")
        
        print("if x > 10:")
        print('  print("Above ten,")')
        print("  if x > 20:")
        print("     print('and also above 20!')")
        print("  else:")
        print('     print("but not above 20.")')

        print("***************************************************************** \n                     -THE PASS STATEMENT- ")
        
        print("if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.")
        
        print("Example of this is ")
        print("a = 33")
        print("b = 200")
        print("if b > a:")
        print("  pass")

if num == "5":

        print("*****************************************************************\n***************************************************************** \n                     -PYTHON FOR LOOPS- ")
        print("       1. Looping Through a String")
        print("       2. The break Statement")
        print("       3. The continue Statement")
        print("       4. The range() Function")
        print("       5. Else in For Loop")
        print("       6. Nested Loops")
        print("       7. The pass Statement")

num3 = input("Enter a number in the PYTHON FOR lOOPS: ")

if num3 == "1":
        print("A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).")

        print("This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.")

        print("With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.")

        print("\n Example")
        print("Print each fruit in a fruit list:")

        print('\nfruits = ["apple", "banana", "cherry"]')
        print("for x in fruits:")
        print("  print(x)")
elif num3 == "2":
        print("THE BREAK STATEMENT")
        print("With the break statement we can stop the loop before it has looped through all the items:")
        print("Example")
        print('Exit the loop when x is "banana":')
        print('fruits = ["apple", "banana", "cherry"]')
        print("for x in fruits:")
        print("  print(x)")
        print('  if x == "banana":')
        print("    break")
elif num3 == "3":
        print(" THE CONTINUE STATEMENT")
        print("With the continue statement we can stop the current iteration of the loop, and continue with the next:")
        print("Example")
        print("Do not print banana:")
        print('fruits = ["apple", "banana", "cherry"]')
        print("for x in fruits:")
        print('  if x == "banana":')
        print("    continue")
        print("  print(x)")

elif num3 == "4":
        print("THE RANGE() FUNCTION ")
        print("To loop through a set of code a specified number of times, we can use the range() function,")
        print("The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.")
        print("Example")
        print("Using the range() function:")
        print("for x in range(6):")
        print("  print(x)")
elif num3 == "5":
        print("ELSE IN FOR LOOP")

        print("The else keyword in a for loop specifies a block of code to be executed when the loop is finished:")
        print("Example")
        print("Print all numbers from 0 to 5, and print a message when the loop has ended:")
        print("for x in range(6):")
        print("  print(x)")
        print("else:")
        print('  print("Finally finished!")')

elif num3 == "6":
        print("NESTED LOOPS")

        print("A nested loop is a loop inside a loop.")

        print('The "inner loop" will be executed one time for each iteration of the "outer loop":')

        print("Example")
        print("Print each adjective for every fruit:")
        print('adj = ["red", "big", "tasty"]')
        print('fruits = ["apple", "banana", "cherry"]')
        print("for x in adj:")
        print("  for y in fruits:")
        print("    print(x, y)")

elif num3 == "7":
        print("THE PASS STATEMENT")
        print("for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.")
        print("Example")
        print("for x in [0, 1, 2]:")
        print("  pass")

if num == "6":
        print("*****************************************************************\n***************************************************************** \n                     -PYTHON LISTS- ")
        
        print("LIST")
        print("Lists are used to store multiple items in a single variable.")
        print("Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.")
        print("Lists are created using square brackets:")


        print("Example")

        print("Create a List:")

        print('thislist = ["apple", "banana", "cherry"]')
        print("print(thislist)")
if num == "7":
        print("*****************************************************************\n***************************************************************** \n                     -FUNCTIONS- ")
        
        print("       1. Creating a function")
        print("       2. Calling a Function")
        print("       3. Arguments")
        print("       4. Number of Arguments")
        print("       5. Arbitrary Arguments, *args")
        print("       6. Keyword Arguments")
        print("       7. Arbitrary Keyword Arguments, **kwargs")
        print("       8. Default Parameter Value")
        print("       9. Passing a List as an Argument")
num4 = input("Enter a number for no. 7 FUNCTIONS: ")

if num4 == "1":
        print("CREATING FUNCTION")
        print("In Python a function is defined using the def keyword:")
        print("Example")
        print("def my_function():")
        print('  print("Hello from a function")')

elif num4 == "2":
        print("CALLING A FUNCTION ")
        print("To call a function, use the function name followed by parenthesis:")
        print("Example")
        print("def my_function():")
        print('  print("Hello from a function")')
        print("my_function()")

elif num4 == "3":
        print("ARGUMENTS")
        print("Information can be passed into functions as arguments.  ")
        print("Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.")
        print("The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:")
        print("Example")
        print("def my_function(fname):")
        print('  print(fname + " Refsnes")')
        print('my_function("Emil")')
        print('my_function("Tobias")')
        print('my_function("Linus")')

elif num4 == "4":
        print("NUMBER OF ARGUMENTS ")
        print("By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.")
        print("Example")
        print('This function expects 2 arguments, and gets 2 arguments:')
        print("def my_function(fname, lname):")
        print("  print(fname + " " + lname)")
        print('my_function("Emil", "Refsnes")')

elif num4 == "5":
        print("ARBITRARY ARGUMENTS, *ARGS")
        print("If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.")
        print("This way the function will receive a tuple of arguments, and can access the items accordingly:")
        print('Example')
        print("If the number of arguments is unknown, add a * before the parameter name:")
        print("def my_function(*kids):")
        print('  print("The youngest child is " + kids[2])')
        print('my_function("Emil", "Tobias", "Linus")')

elif num4 == "6":
        print("KEYWORD ARGUMENTS")
        print("You can also send arguments with the key = value syntax.")
        print("This way the order of the arguments does not matter. ")


        print("Example")
        
        print('def my_function(child3, child2, child1):')

        print('  print("The youngest child is " + child3)')


        print('my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")')
        
elif num4 == "7":
        print("ARBITRARY KEYWORD ARGUMENTS, **kwargs")
        print("If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.")
        print("This way the function will receive a dictionary of arguments, and can access the items accordingly:")
        print("Example")
        print("If the number of keyword arguments is unknown, add a double ** before the parameter name:")

        print('def my_function(**kid):')
        print('  print("His last name is " + kid["lname"])')

        print('my_function(fname = "Tobias", lname = "Refsnes")')
elif num4 == "8":
        print("DEFAULT PARAMETER VALUE")
        print("The following example shows how to use a default parameter value.")
        print("If we call the function without argument, it uses the default value:")
        print("Example")
        print('def my_function(country = "Norway"):')
        print('  print("I am from " + country)')
        print('my_function("Sweden")')
        print('my_function("India")')
        print('my_function()')
        print('my_function("Brazil")')
elif num4 == "9":
        
        print("You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.")

        print("E.g. if you send a List as an argument, it will still be a List when it reaches the function:")

        print("Example")
        print("def my_function(food):")
        print("  for x in food:")
        print("    print(x)")
        print('fruits = ["apple", "banana", "cherry"]')
        print("my_function(fruits)")


# If the user chooses not to start the program:
else:
    print("Thank you for using the program!")