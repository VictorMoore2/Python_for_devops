#index

#python
#012345
""" x="python"
y=x[2]
print(y) """

s = "lovecitygospel"
#index: 0 1 2 3 4 5 6 7 8 9 10 11 12
#letters:l o v e c i t y g o s p e l
""" y= s[4:8]
print(y) """

""" y= s[1:7:4]
print(y) #output:oi """

""" y= s[ : :-1]
print(y) #output: lepsogyticevol """


#using f string
""" name="victormoore"
greeting=f"goodmorning,{name}!"
print(greeting) """

#using .format()
""" age=31
statement = "i am {} years old".format(age)
print(statement) 
"""


#the if condition

""" age= 25
if age >= 18:
    print("you are an adult") """

#elif condition
""" score = 75
if score>= 90:
    print("grade A")
elif score>=80:
    print("grade B")
elif score>=70:
    print("grade C")
else:
    print("grade F") """


""" age=23
if age>=18:
    print("you are an adult")
elif age>=24:
    print("you are not an adult") """

""" first_name = "victor"
last_name = "moore"
full_name = first_name+" "+last_name
print(full_name) """

#not
""" y =4>6
x =not(y)
print(x) """

#indexting
""" s = "victormoore"
#letter = v i c t o r m o o r e
#index = 0 1 2 3 4 5 6 7 8 9 10
y =s[::-1]
print(y) """

""" s = "lexxon"
#letter = l e x x o n
#index = 0 1 2 3 4 5
y =s[2:5]
print(y) """


#temperature converter

#celsuis =(fahrenheit - 32) * 5/9
#fahrenheit =float(input("enter temperature in fahrenheit:"))

#name = input("enter your name")
#print(f"your name reversed is:{name[ : :-1]}")

""" message = input("tell me something, and i will reply you:")
print(message) """

#format{}
""" x = input("what is your name:")
print(f"my name is:{x}") """

""" name = input("enter your name:")
print(f"my name is :{name}")
"""

""" name = input("enter your name:")
print(f"hello,{name}!")
 """

fahrenheit =float(input("enter temp in fahrenheit:"))
celsuis = (fahrenheit -32)* 5/9
print(f"{fahrenheit}F is {celsuis: .2f}c")







