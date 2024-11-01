""" #Global Variable
x = 10 # Global variable

def print_global():
    print(x) #Accessing global variable inside a function

print_global() # Output: 10
 """

#odifying global variable
""" x = 10
def modify_global():
    global x
    x= 5
modify_global()
print(x) """

#default argument
""" def greet(name ="stranger"):
    print(f"Hello ,{name} !")
greet()
greet("victormoore") """

#keyword arguement
""" def introduce(name,age):
    print(f"my name is {name}, i am {age} years old.")
introduce(name ="john",age = 22)
introduce("Alice",32)
introduce(34,"Lexxon") """

#Area Calculator

""" def area_of_circle(radius):
    return 3.14159*radius**2

def area_of_rectangle(width,height):
    return width*height

def main():
    print("choose a shape:1 for circle,2 for rectangle")
    choice =int(input("enter the number of your choice:"))
    
    if choice==1:
        radius = float(input("enter the area_of_the circle:"))
        print(f"The area_of_the circle is {area_of_circle(radius)}")
    elif choice ==2:
        width = int(input("Enter the width of a rectangle:"))
        height = int(input("Enter the height of the rectangle:"))
        print(f"The area of the rectangle is {area_of_rectangle(width,height)}")
    else:
        print("invalid choice")
if __name__=="__main__":
        main() """

#Module
""" import math_utils add,subtract
result = math_utils.add(5,3)
print(result)

result = math_utils.subtract(5,3)
print(result) """


import math
print(math.sqrt(16))