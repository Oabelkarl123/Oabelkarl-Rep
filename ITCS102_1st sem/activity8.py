prelim = eval(input("inout your Prelim Grades:  "))
midterm = eval(input("inout your midtermGrades:  "))
semi_final = eval(input("inout your semi_final Grades:  "))
finals = eval(input("inout your finals Grades:  "))
quiz = eval(input("inout your quiz Grades:  "))
project = eval(input("inout your Project Grades:  "))

finals_grades = (prelim * 0.15 ) + (midterm * 0.15 ) + (semi_final * 0.15 ) + (finals * 0.15 ) + (quiz  * 0.15 ) + (project * 0.15 )

print(f" Your final grade is {final_grades}")

if final_grades >= 75 : 
    print(" Cogratulations, you have pass the course ")
else:
    print("were very sorry to announce that you have failed to pass the course ")