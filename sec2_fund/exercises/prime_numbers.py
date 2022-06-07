# write a program that can determines whether a number is a prime number or not.

for n in range(2, 30 + 1):
  # Check every number below n if it's primal or not
  for x in range(2, n):
    if n % x == 0:
      print(f"{n} is not a primal number. {n} = {x} * {n//x}")
      break
  else:
    print(f"{n} is a primal number.")