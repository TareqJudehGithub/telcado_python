
numbers = [1, 2, 3, 4, 5]

# Double all numbers in numbers list, creating a new list.

# Using for loop
double_numbers = list()

# Iterate over all iterables in numbers list, doubling them, and adding them
# to double_numbers:
for num in numbers:
  double_numbers.append(num * 2)
print(double_numbers, end="\n\n")

# Using list comprehension
#  list_variable = [(expression) (iterable)]
double_figures = [num * 2 for num in numbers]
print(double_figures, end="\n\n")

# Write a problem to find out odd/even numbers giving the range 1 - 20 using 
# list comprehension
print("Odd - Even")
even = [str(num) + " is even" for num in range(2, 20) if num % 2 == 0]
print(even, end="\n\n")

even_odd = [str(num) + " is even" if num % 2 == 0 else str(num) + " is odd" for num in range(2, 20)]
print(even_odd, end="\n\n")

# Re-write primal numbers 1 - 20 problem
for x in range (2, 20):
  for y in range(2, x):
    if x % y == 0:
      print(f"{x} divided by {y} = {x % y}")
      break
    else:
      print(f"{x} is a primal number.")
      break

else:
  print("\nEnd of Primal problem.", end="\n\n")
    

# FizzBuzz 1 - 20
print("FizzBuzz Problem:")
for num in range(21):
  if  num % 3 == 0 and num % 5 == 0 and num > 0:
    print(f"{num} FizzBuzz!")
  elif num % 3 == 0 and num > 0:
    print(f"{num} Fizz!")
  elif num % 5 == 0 and num > 0:
    print(f"{num} Buzz")
print("")



