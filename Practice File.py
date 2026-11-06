'''print("-"*35)
print("----------Budget Info----------")
print("-"*35)
salary=3000
food=2000
mobile=1000
groceries=3000
dress=1000
eb_bill=2000
fuel=2000
pocket_money=4000

Expense=food+mobile+groceries+dress+eb_bill+fuel+pocket_money

print("Person Salary :",salary)
print("Expense Amount :",Expense)
rem_amount=salary-Expense
print("remaining amount :",rem_amount)

#fruit Bill Calculations
#fuirts Price as per KG
apple= 300
banana = 90
chiku = 70
dragon_fruit = 250
watermelon = 90
berry = 180

#Fruits Purchased by Customers
p_apple=3.4
p_banana=4.5
p_chiku=1.8
p_dragon_fruit=3.2
p_watermelon=6.8
p_berry=2.0

ta=((p_apple*apple))
tb=((p_banana*banana))
tc=((p_chiku*chiku))
td=((p_dragon_fruit*dragon_fruit))
tw=((p_watermelon*watermelon))
ty=((p_berry*berry))

P_total=(ta+tb+tc+td+tw+ty)
print("apple cost :",ta)
print("banana cost :",tb)
print("chiku cost :",tc)
print("dragon friut cost :",td)
print("watermelon cost :",tw)
print("Berry cost :",ty)
print("Grand Total :",P_total)'''

'''#Conditional Statement
#if
#if else
#elif
#nested if
if 30>26:
    print("hot")
elif 20>26:
    print("mild")
elif 15>26:
    print("cold")
else:
    print("chill")'''

'''
marks=89
if marks >=80:
    print("Great")
elif marks >=60:
    print("good")
else:
    print("pass")'''

'''regno="A123"
name="Sara"
m1=56
m2=70
m3=67
TT=m1+m2+m3
AVG=TT/3
print("*"*35)
print("*"*12,"Student mark List","*"*12)
print("NAME \t\t\t:",name)
print("Resgistration Number\t:",regno)
print("Average Mark Scored\t:",f"{AVG:.1f}")
if AVG >80:
    print("GRADEt:","O")
elif AVG >70:
    print("GRADE:","A")
elif AVG >60:
    print("GRADE\t\t\t:","B")
elif AVG >50:
    print("GRADE","C")
else:
    print("GRADE","F")'''

a=21
if a%2==0:
    print("even")
else:
    print("odd")

b=-9
if a<0:
    print("Negative")
elif a>0:
    print("Positive")
else:
    print("0")

c="yellow"
if c=="Green":
    print("GO")
elif c=="yellow":
    print("Caution")
else:
    print("STOP")

d=401
if d<=200:
    print("no Bill")
elif d>=201 and d<=400:
    print("5.6 Rs Per Unit")
else:
    print("8 Rs Per Unit")

age=16
citizen="India"
if age>=18 and citizen=="India":
    print("Eligble to Vote ")
else:
    print("NoT Eligle Given")
