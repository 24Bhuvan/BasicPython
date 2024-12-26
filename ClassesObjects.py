#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.
#Creating a class
class Myclass:
    x = 5
    def function(self):
        print("This is a message inside the class.")
#Creating an object
p1 = Myclass()#have to store template of class in a variable
print(p1.x)

#To access a function inside of an object you use notation similar to accessing a variable:
p1.function()
#__init__() Function
class Person:
  def __init__(self, name, age):#All classes have a function called __init__(), which is always executed when the class is being initiated.
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#The __str__() function controls what should be returned when the class object is represented as a string.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)


#A simple example for class and objects in python
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())