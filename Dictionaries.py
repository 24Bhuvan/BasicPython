#Dicationaries are mutable and unindexed 
#Creating dictionaries
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)
#Alternate method
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)
#Accessing values in a dictionary
print(phonebook["John"])
#to know how many items in a dictionary
print(len(phonebook))
#The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
#From data type perspective, dictionaries are defined as objects with the data type 'dict':
print(type(thisdict))
#It is also possible to use the dict() constructor to make a dictionary.
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)