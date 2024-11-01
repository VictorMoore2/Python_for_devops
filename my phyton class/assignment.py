""" result=(2+4)
print(result) """

""" #asssignment
ade=(5)
john=(6)
age=int(ade + john)
print(age) """

""" x=(4)
y=(17)
z=int(x+y)
print(z)  #output: 21 """


""" number=int(input("enter a number:"))
print(number) """

#assignment

""" user_one=int(input("enter a number:"))
print(user_one) """

""" user_two=int(input("enter a number:"))
print(user_two) """

#assignment
""" x= int(input("enter the first number:"))
y= int(input("enter the second number:"))
z=(x+y)
print(z)  """ 
# #output:8,where x is 4 and y is 


#simple calculator

num1 =float(input("enter first number:"))
num2 =float(input("enter second number:"))
operator = input("enter an operator(+,-,*,/):")
if operator=="+":
    print(f"result:{num1  + num2}")
elif operator=="-":
    print(f"result:{num1  - num2}")
elif operator=="*":
    print(f"result:{num1  * num2}")
elif operator=="/":
    print(f"result:{num1  / num2}")
elif operator=="//":
    print(f"result:{num1  // num2}")
elif operator=="%":
    print(f"result:{num1  % num2}")
else:
    print("invalid operator")
