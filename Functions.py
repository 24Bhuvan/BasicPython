#Defining a function 
def my_function():
    print("Hello From My Function!")
#Using arguments in a function 
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
#Functions may return a value to the caller, using the keyword- 'return' . For example:
def sum_two_numbers(a, b):
    return a + b
#Calling functions in python
my_function()
my_function_with_args("John Doe", "a great year!")
x = sum_two_numbers(1,2)

#Here an example where we explain the benefits of functions
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit
def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
