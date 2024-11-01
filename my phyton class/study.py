#NESTED LIST

""" matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    for element in row:
        print(element)
 """

#BREAK
""" for num in range(1,8):
    if num ==5:
        break
    print(num) """

#temperature converter
""" fahrenheit =float(input("enter temp in fahrenheit"))
celsuis= (fahrenheit-32)* 5/9
print(f"{fahrenheit}Fis{celsuis: .2f}c)")
 """

""" count = 1
while count<=5:
    print(f"count is {count}")
    count+=1 """
    
#if condition
""" age= 20
if age>=18:
    print("you are older,and eligible to vote") """

""" x= int(input("enter your age_1:"))
y=int(input("enter your age_2:"))
z=(x+y)
print(z) """

#if- else condition
""" score =80
if score>=70:
    print("grade_ A")
else:
    print("grade_B")
 """

#if condition
""" age= 18
if age>= 18:
    print("you are an adult")
    print("you are strong") """

#if-elif-else condition
""" age =15
if age<4:
    print("your admission is $0")
elif age<18:
    print("your admission is $25")
else:
    print("your admission is $40") """

""" fahrenheit = float(input("enter temperarature in celsuis:"))
fahrenheit=("celsuis"*9/5)+32
print(f"{"celsuis"}C is {"fahrenheit"} .2f") """

""" 
age= input("how old are you?:")
print(f"hello, {age}") """


""" age=input("how old are you?:")
print(age) """

#concatenation
""" first_name = "john"
last_name ="moore"
full_name =first_name+" "+last_name
print(full_name)
 """

 #modolus
""" x = 10%3
print(x) """

#floor division
""" x = 10//3
print(x) """

""" for number in range (1,11):
    if number ==7:
        break
    print(number) """

""" celsuis =float(input("enter temp in celsuis:"))
fahreheit =(celsuis*(9/5)) + 32
print(f"{"celsuis"}c is {"fahrenheit": .2f}f") """


#converting celsuis to fahrenheit

""" celsuis = float(input("enter temp in celsuis: "))
fahrenheit =(celsuis*(9/5)) + 32
print(f"{celsuis: .2f}C is {fahrenheit}F") """

#continue statement

""" for num in range(1,6):
    if num ==3:
        continue
    print(num) """

    #pass statement

   #"""  for num in range(1,6):
#if num ==3:
 #       pass
    #print(num) """


#sending a reminder email


          



  #Processing file in a directory

""" import os
directory = "/Users/hp/Desktop/MY WEDDING/UNEDITED PICTURES"
for filename in os.listdir (directory):
    if filename .endswith(".jpg"):
        print(f"processing {directory}") """
   

#simple calculator

""" num1 =float(input("enter first number:"))
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
    print("invalid operator")  """


#Multiplication Table
""" for i in range (1,6):
    for j in range(1,6):'
        print(f"{i} x {j}= {i*j}")

        print()
 """

#name,age = "victor",43


#guest = ["samuel","mummy_uche","mama_jekwu"]
#print(guest)
#print(f"Hello!,{guest[0]}, am inviting you to my wedding ceremony")
#print(f"Hello!,{guest[1]}, am inviting you to my wedding ceremony")
#print(f"Hello!,{guest[2]}, am inviting you to my wedding ceremony")

""" del guest[0]
print(guest) """

#cars = ["benz","toyota","lexus","acura"]
#print(cars)
#cars.reverse()
#print(cars)
#cars.sort()
#print(cars)
""" print(f"{cars[0]} is better than {cars[-1]}")
len(cars)
print(cars[0]) """

person = {"age" : 30,"name" : "victor","address" : "no 2 ifememzie"}
""" #person["address"] = "ochanja"
print(person)

#person["address"] = "kogi"
print(person)
#del person["name"]
print(person)
#person.pop("age")
print(person)
 """
#print(person.items())

""" cars =["benz","acura", "toyota","honda"]
for car in cars[2]:
    print(car.title()) """

#functions

""" def greet(username):
    print(f"Hello,{username}")
greet("victor_moore") """

""" def greet():
    print("hello")
greet() """


""" #nested dictionaries
students = {"student1":{"name" : "victor","age" :22},
"student2" :{"name" : "lexxon","age" : 34}
}
print(students["student1"]["name"],students["student2"]["name"])

 """

""" persons ={"ebube":31,"ebele":29,"chiamaka":27,"amala":25,"gozie":22,"somtoo":19
}
print(persons["amala"])
for person in person:
    print(f"i love {"amala"}")

persons["amala"] = 30
print(persons)

print(persons["chiamaka"]) """

""" fruits = ["apple","oranges","cashew","grape"]
for fruit in fruits:
    print(f"i like {fruit}") """

""" cars ={"honda" :2,"benz" : 10}
print(cars)

cars["babrus"] = 12
cars["acura"] = 199
print(cars) """

""" 
cars ={}
cars["honda"] = 3
cars["benz"] = 44
print(cars)

print(f" i love {cars}") """

""" cars = {"c_class" : 3,"g_guard" :4,"s_class" :5}
print(cars)
#print(f" i love {cars["g_guard"]}")
del cars["c_class"]
print(cars) """

""" cars ={"benz" : 7,
    "toyota" : 3,
    "honda" : 19,
    "lexus" : 29
}
 """


""" def area_of_circle(radius):
    return 3.14159 * radius ** 2

def area_of_rectangle(width, height):
    return width*height

def main():
    print("Choose a shape: 1 for  Circle,  2 for Rectangle")
    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is {area_of_circle(radius)}")
    elif choice == 2:
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        print(f"The area of the rectangle is {area_of_rectangle(width, height)}")
    else:
        print("Invaild choice!")

if __name__ == "__main__":
    main()
 """

""" def celsuis_to_fahrenheit(c):
    return (c*9/5)+32
temp = float(input("Enter the temp in celsuis(c):"))
print({temp}) """

import requests
#Making a get request
r = requests.get("https://www.geeksforgeeks.org/python-web-scraping-tutorial/")
print(r.content)



   
