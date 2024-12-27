#Using a function from another module
import Modules1

#Renaming a module
import Modules1 as ms

#From another module can directly import the function we want
from Modules1 import greeting

#From another module can directly import the varible we want of any data type
from Modules1 import person1


#Accessing functions from module
Modules1.greeting("Jonathan")

#The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc)
#Accesing values in a dictionary from another module
print(Modules1.person1["name"])