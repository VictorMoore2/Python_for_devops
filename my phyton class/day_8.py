#Object-Oriented Programming (OOP) Concepts
""" class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog('Bingo', 5)
my_dog.sit()
my_dog.roll_over() """


""" class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print(f"{self.brand} {self.model} {self.year}")
my_car = Car("Benzoo", "GLE",2025)
my_car.display_info() """

#Encapsulation

""" class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance #private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")
    
    def get_balance(self):
        return self.__balance
    
account = BankAccount('John Doe', 1000)
account.deposit(500)
account.withdraw(300)
print(account.get_balance()) #Output 1200 """

#Inheritance
""" class Vehicle:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    def start(self):
        print("The vehicle is starting")

class Car(Vehicle):
    def __init__(self,brand,model,year):
        super().__init__(brand,year)
        self.model = model
    
    def honk(self):
        print("The car is honking")

my_car = Car("Benz","Glk",2024)
my_car.start()
my_car.honk()
 """
#Polymorphism
""" class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"

animals = [Dog(),Cat()]
for animal in animals:
    print(animal.sound()) """

#Abstraction
#check your note or tutuor's whatsapp

#Example1: 
#E-commerce system

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def display_product(self):
        print(f" Product: {self.name},Price: ${self.price}")

class ShoppingChart:
    def __init__(self):
        self.items =[]
    
    def add_item(self,product):
        self.items.append(product)
        print(f"Added {product.name} to the cart")

    def remove_item(self,product):
        self.items.remove(product)
        print(f"Removed {product.name} from the cart.")

    def total_price(self):
        return sum(item.price for item in self.items)
    
product1 = Product("Laptop",1200)
product2 = Product("Headset",500)

cart = ShoppingChart()
cart.add_item(product1)
cart.add_item(product2)

print(f"Total price: ${cart.total_price()}")
