#Area Calculator
#finding the area of square and a triangle
#project 1

""" def area_of_square(side):
    return side**2

def area_of_triangle(breadth,height):
    return 0.5*breadth*height

def main():
    print("choose a shape: 1 for square,2 for triangle")
    choice = int(input("Enter the number of your choice:"))
    if choice ==1:
        side =int(input("Enter the nside of the square:"))
        print(f"The area of the square is {area_of_square(side**2)}")

    elif choice==2:
        breadth =float(input("Enter the breadth of the triangle:"))
        height =float(input("Enter the height of the triangle:"))
        print(f"The area of the tiangle is {area_of_triangle(breadth,height)}")

    else:
        print("invalid choice")

if __name__=="__main__":
    main()  """


#finding the area of a circle and a rectangle
#project 2

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
    main() """

#finding the area of a parallelogram,trapezoid and ellipse
#Project 3

""" def area_of_a_parallelogram(base,height):
    return base *height
def area_of_trapezoid(base_1,base_2,height):
    return ((base_1 + base_2)/2)*height
def area_of_an_ellipse(lenght_1,lenght_2):
    return 3.14159*lenght_1*lenght_2

def main():
    print("choose the shape: 1 for parallelogram,2 for trapezoid,3 for ellipse")
    choice = float(input("Enter the number of the choice:"))
    if choice ==1:
        base = float(input("Enter the base of the parallelogram:"))
        height = float(input("Enter the height of a parallelogram:"))
        print(f"The area of a parallelogram is {area_of_a_parallelogram(base,height)}")
    elif choice ==2:
        base_1 =float(input("Enter the first base of the trapezoid:"))
        base_2 = float(input("Enter the second base of the trapezoid:"))
        height =float(input("Enter the height of the trapezoid:"))
        print(f"The area of the trapezoid is {((base_1 + base_2)/2)*height}")
    elif choice ==3:
        lenght_1 = float(input("Enter the first lenght of the ellipse:"))
        lenght_2 = float(input("Ennter the second lenght of the ellipse:"))
        print(f"The area of a ellipse is {3.14159*lenght_1*lenght_2}")
    else:
        print("invalid choice")
if __name__ == "__main__":
    main() """

        

""" #finding the area of a square,triangle,circle,rectangle,
# parallelogram,trapezoid and ellipse
#project 4

def area_of_square(side):
    return side**2

def area_of_triangle(breadth,height):
    return 0.5*breadth*height

def area_of_circle(radius):
    return 3.14159 * radius ** 2

def area_of_rectangle(width, height):
    return width*height

def area_of_a_parallelogram(base,height):
    return base *height

def area_of_trapezoid(base_1,base_2,height):
    return ((base_1 + base_2)/2)*height

def area_of_an_ellipse(lenght_1,lenght_2):
    return 3.14159*lenght_1*lenght_2

def main():
    print("choose the shape:1 for square,2 for triangle,3 for circle,4 for rectangle, 5 for parallelogram,6 for trapezoid,7 for ellipse")
    choice = float(input("Enter the number of the choice:"))

    if choice ==1:
        side =int(input("Enter the side of the square:"))
        print(f"The area of the square is {area_of_square(side)}")

    elif choice==2:
        breadth =float(input("Enter the breadth of the triangle:"))
        height =float(input("Enter the height of the triangle:"))
        print(f"The area of the tiangle is {area_of_triangle(breadth,height)}")

    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is {area_of_circle(radius)}")
    elif choice == 4:
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        print(f"The area of the rectangle is {area_of_rectangle(width, height)}")
    elif choice ==5:
        base = float(input("Enter the base of the parallelogram:"))
        height = float(input("Enter the height of a parallelogram:"))
        print(f"The area of a parallelogram is {area_of_a_parallelogram(base,height)}")
    elif choice ==6:
        base_1 =float(input("Enter the first base of the trapezoid:"))
        base_2 = float(input("Enter the second base of the trapezoid:"))
        height =float(input("Enter the height of the trapezoid:"))
        print(f"The area of the trapezoid is {((base_1 + base_2)/2)*height}")
    elif choice ==7:
        lenght_1 = float(input("Enter the first lenght of the ellipse:"))
        lenght_2 = float(input("Ennter the second lenght of the ellipse:"))
        print(f"The area of a ellipse is {3.14159*lenght_1*lenght_2}")
    else:
        print("invalid choice")
if __name__ == "__main__":
    main() """


#Temperature Converter
#Project 5

def celsuis_to_fahrenheit(c):
    return (c*9/5)+32

def fahrenheit_to_celsuis(f):
    return (f-32)*5/9

def celsuis_to_kelvin(c):
    return c +273.15

def fahrenheit_to_kelvin(f):
    return (f-32)*5/9+273.15

def kelvin_to_celsuis(k):
    return k -273.15

def kelvin_to_fahrenheit(k):
    return (k -273.15)*9/5+32

def temperature_converter():
    print("choose the conversion:")
    print("1 for celsuis_to_fahrenheit:")
    print("2 for fahrenheit_to_celsuis:")
    print("3 for celsuis_to_kelvin:")
    print("4 for fahrenheit_to_kelvin:")
    print("5 for kelvin_to_celsuis:")
    print("6 for kelvin_to_fahrenheit:")

    choice = float(input("Enter yor choice:"))
    temp = float(input("Enter the temp to converter:"))

    if choice == 1:
        print(f"{temp}c is {celsuis_to_fahrenheit(temp)}f")
    elif choice ==2:
        print(f"{temp}f is {fahrenheit_to_celsuis(temp)}c")
    elif choice ==3:
        print(f"{temp}c is {celsuis_to_kelvin(temp)}k")
    elif choice ==4:
        print(f"{temp}c is {fahrenheit_to_kelvin(temp)}k")
    elif choice ==5:
        print(f"{temp}c is {kelvin_to_celsuis(temp)}k")
    elif choice ==6:
        print(f"{temp}k is {kelvin_to_fahrenheit(temp)}c")
    else:
        print("invalid choice")

if __name__=="__main__":
    temperature_converter()
