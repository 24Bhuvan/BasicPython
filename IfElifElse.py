def check_number(num):
  """
  This function checks if a given number is positive, negative, or zero.

  Args:
    num: The number to be checked.

  Returns:
    A string indicating whether the number is positive, negative, or zero.
  """

  if num > 0:
    return "Positive"
  elif num < 0:
    return "Negative"
  else:
    return "Zero"

# Get input from the user
number = float(input("Enter a number: "))

# Call the function and print the result
result = check_number(number)
print(f"The number is {result}.")