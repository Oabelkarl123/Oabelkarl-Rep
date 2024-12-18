prelim = eval(input("PRELIM GRADE : "))
midterm = eval(input("MIDTERM GRADE : "))
sfinals = eval(input("SEMI FINALS GRADE : "))
finals= eval(input("FINALS GRADE : "))
quiz = eval(input("QUIZ GRADE : "))
project = eval(input("PROJECT GRADE : "))

fg = (prelim * 0.15) + (midterm * 0.15) + (sfinals * 0.15) + (finals * 0.15) + (quiz * 0.25) + (project * 0.15)

if fg >= 75 : 
	print("congratulations, you passsed the subject")

else: 
	print ("sorry, but you did not passed the subject")

