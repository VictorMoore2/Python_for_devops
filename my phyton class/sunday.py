#list, tuple and set

#list
""" fruits= ["apple,mangoes""banana"]
       
number= [1,2,3,4,5]
matrix = [[3,5],[3,5],[3,5]]
 """
#indexing and slicing list

#fruits= ["apple","mangoes","banana"]
#print(fruits[0]) #output:apple
#print(fruits[1:3]) #output:mangoes,banana
#print(fruits[-1]) #output:banana
#print(fruits[1]) #output:apple

#modifying  list
#using append()
#fruits.append("orange")
#print(fruits)

#using insert()
""" fruits.insert(2,"orange")
print(fruits) """

#removing items
#remove()
#pop()
#clear()

""" fruits.remove("apple")
print(fruits)
 """
#using pop()
""" 
fruits.pop(2)
print(fruits) """

#using clear()

""" fruits.clear()
print(fruits) """

#sorting lists
#sort() ascending order

#numbers = [1,5,2,3,4,8,9,7]
""" numbers.sort()
print(numbers) """

#descending order
""" numbers.sort(reverse=True)
print(numbers) """


#list comprehension
""" squares = [x**3 for x in range(10)]
print(squares) """

""" squares = [x**2 for x in (1,2,3,4)]
print(squares)

squares =[]
for x in (1,2,3,4):
    squares.append(x**2)
    print(squares) """

""" squares = [x**2 for x in (1,2,3,4)]
print(squares) """

""" squares = []
for x in (1,2,3,4):
    squares.append(x**2)
print(squares) """

""" evens =[x for x in range(10) if x % 2==0]
print(evens) """

""" odd =[x for x in range(10) if x % 2!=0]
print(odd)

even= []
for x in range(10):
    if x %2==0:
        even.append(x)
        print(even) """


#tuple
""" color = ["red","green","blue"]
print(color[0])
print(color[1:]) """

#tuple unpacking

""" person = ("john",23,"engineer")
name,age,profession = person
print(name)
print(age)
print(profession) """

""" squares = []
for x in (2,3,5,6):
    squares.append(x**3)
    print(squares """

""" even =[]
for x in range (16):
    if x % 3==0:
        even.append(x)
        print(even) """

cars = ("benz","honda","lexus","toyota")
print(len(cars))