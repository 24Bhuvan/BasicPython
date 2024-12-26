def loop_demo():
  """Demonstrates the usage of for, while, break, and continue loops."""

  print("\n--- For Loop ---")
  # Iterate through a list of numbers
  numbers = [1, 2, 3, 4, 5]
  for num in numbers:
    print(num)

  print("\n--- While Loop ---")
  count = 0
  while count < 5:
    print(count)
    count += 1

  print("\n--- Break Statement ---")
  for num in range(10):
    if num == 5:
      break  # Exit the loop when num is 5
    print(num)

  print("\n--- Continue Statement ---")
  for num in range(10):
    if num % 2 == 0:  # Skip even numbers
      continue
    print(num)

if __name__ == "__main__":
  loop_demo()