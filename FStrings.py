#To specify a string as an f-string, simply put an f in front of the string literal, like this:
Name = "Bhuvan Ummidisetti"
Age = 18
print(f"The name is {Name}. Age is {Age}")

#Note:To format values in an f-string, add placeholders {} 
#A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
print(f"The age using modifiers {Age:.2f}")

#Direct formatting without using variables
print(f"The age without keeping values in variable is {18:2f}")

#Performing operations on F-Strings
price= 30
tax = 0.20
print(f"Total value of asset is {price + (price*tax)}")

#if..else in F-String
print(f"It is expensive {'Expensive' if price>50 else 'cheap'}")

#Functions in F-strings
print(F"The in Capital case {Name.upper()}")\

#Before Python 3.6 we used the format() method to format strings.
#Indexing using format() function
father_age = 50
father_name = "Gopi Ummidisetti"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(father_age,father_name))