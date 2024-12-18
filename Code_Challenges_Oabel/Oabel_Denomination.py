amount = eval(input("Enter an amount--> "))
name = input("what is your name--> ")

# 1,879


thousand =  amount // 1000
thousand_sukli = amount % 1000
fh = thousand_sukli // 500
fh_sukli = thousand_sukli % 500
hh = fh_sukli // 200
hh_sukli = fh_sukli % 200
h = hh_sukli // 100
h_sukli = hh_sukli % 100
f = h_sukli // 50
f_sukli = h_sukli % 50
tt = f_sukli // 20
tt_sukli = f_sukli % 20
t = tt_sukli // 10
t_sukli = tt_sukli % 10
p = t_sukli // 5
p_sukli = t_sukli % 5
o = p_sukli //1
o_sukli = p_sukli % 1

print("hi, "+name+" your denomination exchange in PH are as follow")
print(thousand,  " - 1000")
print(fh,  "-500" )
print(hh,  "-200")
print(h,  "-100")
print(f,  "-50")
print(tt,  "-20")
print(t,  "-10")
print(p,  "-5")
print(o, "-1")